# Capstone Project Specification

## AI-Powered Text Summarizer Web Application

**Course:** COP 2501  
**Project type:** Capstone  
**Delivery:** Web application with REST API backend

---

## 1. Problem Statement

Users often need concise summaries of long articles, notes, or documents. Manual summarization is slow and inconsistent. This application accepts pasted text and returns a shorter summary using NLP-based extractive summarization.

## 2. Goals

| Goal | Success criteria |
|------|------------------|
| Accept user text input | Text area supports multi-paragraph input |
| Generate summaries | API returns summary in under 5 seconds for typical input |
| Configurable length | User selects sentence count (3, 5, or 7) |
| Clear UI | Responsive layout, readable typography, error feedback |
| Runnable locally | Single-command setup with documented dependencies |

## 3. Non-Goals

- User accounts or authentication
- File upload (paste-only for v1)
- Abstractive / LLM API integration (optional future enhancement)
- Mobile native apps

## 4. Architecture

```
┌─────────────┐     POST /api/summarize      ┌──────────────┐
│  Browser    │ ───────────────────────────► │  Flask API   │
│  (HTML/JS)  │ ◄─────────────────────────── │  + Sumy/NLP  │
└─────────────┘     JSON { summary, meta }   └──────────────┘
```

### Stack

| Layer | Technology | Rationale |
|-------|------------|-----------|
| Frontend | HTML, CSS, vanilla JS | No build step; easy to demo |
| Backend | Python 3.10+, Flask | Common in intro CS; simple REST |
| Summarization | Sumy (TextRank) + NLTK | Lightweight, no API keys |
| Data | None (stateless) | Simplifies deployment |

## 5. API Design

### `POST /api/summarize`

**Request body (JSON):**

```json
{
  "text": "Long article text...",
  "sentences": 5
}
```

**Response (200):**

```json
{
  "summary": "Condensed summary text.",
  "input_words": 842,
  "summary_sentences": 5,
  "algorithm": "TextRank"
}
```

**Errors:**

| Code | Condition |
|------|-----------|
| 400 | Missing/empty text, invalid sentence count |
| 413 | Text exceeds 10,000 words |
| 500 | Summarization failure |

### `GET /api/health`

Returns `{ "status": "ok" }` for readiness checks.

## 6. UI Requirements

1. Header with project title and short description
2. Large text input for source material
3. Sentence-count selector (3 / 5 / 7)
4. **Summarize** button with loading state
5. Summary output panel with word/sentence stats
6. Error banner for validation and server errors

## 7. Project Structure

```
Capstone-Project-Specification/
├── SPECIFICATION.md          # This document
├── README.md                 # Setup and run instructions
├── requirements.txt
├── backend/
│   ├── app.py                # Flask routes
│   └── summarizer.py         # TextRank wrapper
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── app.js
└── .cursor/
    └── skills/
        └── capstone-plan-build/
            └── SKILL.md      # Plan → Build workflow
```

## 8. Implementation Phases

### Phase 1 — Backend (Build)

- [x] Flask app with CORS for local dev
- [x] Summarizer module using Sumy TextRank
- [x] Input validation and word limits
- [x] Health endpoint

### Phase 2 — Frontend (Build)

- [x] Static UI served by Flask
- [x] Fetch API integration
- [x] Loading and error states

### Phase 3 — Polish

- [ ] README with demo screenshots
- [ ] Optional: Docker or deploy notes
- [ ] Optional: OpenAI abstractive mode behind env flag

## 9. Testing Plan

| Test | Method |
|------|--------|
| Empty input rejected | POST with `""` → 400 |
| Short text handled | 2-sentence input → returns best-effort summary |
| Long text capped | >10k words → 413 |
| UI flow | Paste sample article → summary appears |
| Health check | `GET /api/health` → 200 |

## 10. Sample Demo Text

Use a 3–5 paragraph news-style article (200–800 words) during presentation to show before/after compression.

## 11. Future Enhancements

- PDF/text file upload
- Multiple algorithms (LSA, LexRank) with comparison view
- OpenAI or local LLM for abstractive summaries
- Summary history in browser localStorage
