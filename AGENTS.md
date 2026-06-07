---
title: FreeTheTeacher Repo Rules
id: agents-freetheteacher
version: 1.0.0
status: active
owner: Dakota Hollmann
maintainer: claude-cowork
created: 2026-06-07
updated: 2026-06-07
scope: repo-local — adds to (and inside this repo, overrides) ~/agents/AGENTS.md
changelog:
  - "1.0.0 (2026-06-07): Initial per-repo AGENTS.md — Phase 2 of the AI-first reorg."
---

# FreeTheTeacher — Repo Rules for Agents

Dormant personal full-stack Python project: a modular classroom-management app built as a learning exercise.

## Layout

| Path | Purpose |
|---|---|
| `FreeTheTeacher/src/` | Application modules: attendance, roster, admin, gradebook, messaging, reports, main.py |
| `tests/` | pytest test suite |
| `migrations/` + `alembic.ini` | Alembic database migrations |
| `requirements.txt` | Python dependencies |
| `FreeTheTeacher/` (nested) | Legacy nesting quirk: also contains setup.py, LICENSE, README — do not confuse with `src/` |

## Conventions

- Status: **dormant**. This repo documents a learning journey. Make surgical, targeted changes only — do not refactor, modernize, or restructure.
- Preserve the existing code style and structure even if it is non-idiomatic; it reflects the learning state at time of writing.
- New work must fit the existing module boundaries in `src/`.

## Hazards

- Split layout quirk: the inner `FreeTheTeacher/` dir holds the package (src/, setup.py, LICENSE, README) while `tests/`, `migrations/`, `alembic.ini`, and `requirements.txt` sit at the repo root. Don't "fix" this split; paths in configs assume it.

## Commands

```
pip install -r requirements.txt
pytest
alembic upgrade head
```
