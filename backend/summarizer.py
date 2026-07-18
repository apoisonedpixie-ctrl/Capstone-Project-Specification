"""Abstractive text summarization using Groq Llama 3."""

from __future__ import annotations

import os
import re

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

MODEL = "llama3-8b-8192"
MAX_WORDS = 10_000
ALLOWED_SENTENCE_COUNTS = {3, 5, 7}


def count_words(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text))


def validate_input(text: str, sentences: int) -> str | None:
    if not text or not text.strip():
        return "Text is required."

    if sentences not in ALLOWED_SENTENCE_COUNTS:
        return f"Sentence count must be one of {sorted(ALLOWED_SENTENCE_COUNTS)}."

    if count_words(text) > MAX_WORDS:
        return f"Text exceeds the {MAX_WORDS:,}-word limit."

    return None


def _get_client() -> Groq:
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is not set. Add it to your environment or a .env file."
        )
    return Groq(api_key=api_key)


def generate_summary(text: str, sentences: int = 5) -> str:
    client = _get_client()

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You summarize text clearly and accurately. "
                    "Return only the summary with no labels or preamble."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Summarize the following text in exactly {sentences} "
                    f"complete sentences.\n\n{text.strip()}"
                ),
            },
        ],
        temperature=0.3,
        max_tokens=1024,
    )

    summary = response.choices[0].message.content
    if not summary or not summary.strip():
        raise RuntimeError("Groq returned an empty summary.")

    return summary.strip()
