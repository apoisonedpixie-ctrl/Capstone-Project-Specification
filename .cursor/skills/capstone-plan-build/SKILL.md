---
name: capstone-plan-build
description: >-
  Guides Plan then Build workflow for the COP 2501 AI Text Summarizer capstone.
  Use when planning features, implementing the app, or when the user says Plan,
  Build, / for skills, or @ for context.
disable-model-invocation: true
---

# Capstone Plan → Build

Plan, Build, / for skills, @ for context

## Plan

1. Read `@SPECIFICATION.md` before changing scope or architecture.
2. Confirm the request maps to a spec section (API, UI, validation, polish).
3. If requirements are missing, propose updates to `SPECIFICATION.md` first.
4. Output a short plan: goal, files to touch, risks, test steps.

## Build

1. Implement the smallest diff that satisfies the plan.
2. Match existing stack: Flask backend, vanilla JS frontend, Sumy TextRank.
3. Run locally from `backend/` with `python app.py` after dependency install.
4. Verify: health check, empty-input 400, sample article summarizes.

## Context (`@`)

Attach files that define truth for the task:

| Context | When to attach |
|---------|----------------|
| `@SPECIFICATION.md` | Scope, API, or architecture decisions |
| `@README.md` | Setup, run, or project overview |
| `@backend/app.py` | Routes, CORS, static serving |
| `@backend/summarizer.py` | NLP logic, validation limits |
| `@frontend/` | UI, styling, client behavior |

## Skills (`/`)

| Skill | Use for |
|-------|---------|
| `/capstone-plan-build` | This workflow |
| `/create-skill` | New project skills |
| `/create-rule` | Persistent `.cursor/rules` conventions |

## Checklist

```
- [ ] Plan references SPECIFICATION.md
- [ ] Build stays within capstone non-goals (no auth, no file upload v1)
- [ ] API errors are user-readable JSON
- [ ] README updated if setup or usage changed
```
