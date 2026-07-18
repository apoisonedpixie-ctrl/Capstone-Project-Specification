"""Extractive text summarization using Sumy TextRank."""

from __future__ import annotations

import re

import nltk

from sumy.nlp.stemmers import Stemmer
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.utils import get_stop_words

LANGUAGE = "english"
MAX_WORDS = 10_000
ALLOWED_SENTENCE_COUNTS = {3, 5, 7}


def _ensure_nltk_data() -> None:
    for resource in ("punkt", "punkt_tab", "stopwords"):
        nltk.download(resource, quiet=True)


_ensure_nltk_data()


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


def summarize_text(text: str, sentences: int = 5) -> str:
    parser = PlaintextParser.from_string(text, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    summarizer = TextRankSummarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    available = len(parser.document.sentences)
    target = min(sentences, max(available, 1))

    summary_sentences = summarizer(parser.document, target)
    return " ".join(str(sentence) for sentence in summary_sentences)
