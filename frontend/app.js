const sourceText = document.getElementById("source-text");
const sentenceCount = document.getElementById("sentence-count");
const summarizeBtn = document.getElementById("summarize-btn");
const errorMessage = document.getElementById("error-message");
const outputPanel = document.getElementById("output-panel");
const summaryText = document.getElementById("summary-text");
const summaryMeta = document.getElementById("summary-meta");

function showError(message) {
  errorMessage.textContent = message;
  errorMessage.classList.remove("hidden");
}

function clearError() {
  errorMessage.textContent = "";
  errorMessage.classList.add("hidden");
}

async function summarize() {
  clearError();
  outputPanel.classList.add("hidden");

  const text = sourceText.value.trim();
  if (!text) {
    showError("Please paste some text to summarize.");
    return;
  }

  summarizeBtn.disabled = true;
  summarizeBtn.textContent = "Summarizing...";

  try {
    const response = await fetch("/api/summarize", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        text,
        sentences: Number(sentenceCount.value),
      }),
    });

    const data = await response.json();

    if (!response.ok) {
      showError(data.error || "Something went wrong.");
      return;
    }

    summaryText.textContent = data.summary;
    summaryMeta.textContent = `${data.input_words} words in · ${data.summary_sentences} sentences out · ${data.algorithm}`;
    outputPanel.classList.remove("hidden");
  } catch (error) {
    showError("Could not reach the server. Is the Flask app running?");
  } finally {
    summarizeBtn.disabled = false;
    summarizeBtn.textContent = "Summarize";
  }
}

summarizeBtn.addEventListener("click", summarize);

sourceText.addEventListener("keydown", (event) => {
  if ((event.ctrlKey || event.metaKey) && event.key === "Enter") {
    summarize();
  }
});
