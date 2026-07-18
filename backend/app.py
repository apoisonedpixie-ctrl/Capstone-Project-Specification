"""Flask API for the AI-powered text summarizer."""

from __future__ import annotations

import os
from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

from summarizer import count_words, generate_summary, validate_input

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR.parent / "frontend"

app = Flask(__name__, static_folder=str(FRONTEND_DIR), static_url_path="")
CORS(app)


@app.get("/api/health")
def health():
    return jsonify({"status": "ok"})


@app.post("/api/summarize")
def summarize():
    payload = request.get_json(silent=True) or {}
    text = payload.get("text", "")
    sentences = payload.get("sentences", 5)

    try:
        sentences = int(sentences)
    except (TypeError, ValueError):
        return jsonify({"error": "Sentence count must be a number."}), 400

    error = validate_input(text, sentences)
    if error:
        status = 413 if "word limit" in error else 400
        return jsonify({"error": error}), status

    try:
        summary = generate_summary(text.strip(), sentences)
    except Exception as exc:
        return jsonify({"error": f"Summarization failed: {exc}"}), 500

    return jsonify(
        {
            "summary": summary,
            "input_words": count_words(text),
            "summary_sentences": sentences,
            "algorithm": "Groq Llama 3 8B",
        }
    )


@app.get("/")
def index():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.get("/<path:filename>")
def frontend_assets(filename: str):
    return send_from_directory(FRONTEND_DIR, filename)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
