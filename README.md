# AI-Powered Text Summarizer

COP 2501 capstone web application that summarizes pasted text using extractive NLP (TextRank via Sumy).

## Quick start

```bash
py -3 -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
cd backend
python app.py
```

Open [http://localhost:5000](http://localhost:5000).

## Project docs

- [SPECIFICATION.md](SPECIFICATION.md) — architecture, API, and testing plan

## API

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/health` | Health check |
| POST | `/api/summarize` | Summarize JSON `{ "text": "...", "sentences": 5 }` |

## Cursor workflow

Use the project skill **`/capstone-plan-build`** for the Plan → Build loop:

- **Plan** — design against `@SPECIFICATION.md`
- **Build** — implement backend/frontend
- **`/`** — invoke skills (e.g. `/capstone-plan-build`, `/create-skill`)
- **`@`** — attach context (e.g. `@README.md`, `@backend/app.py`)

## Structure

```
backend/     Flask API + summarizer
frontend/    Static HTML/CSS/JS UI
```
