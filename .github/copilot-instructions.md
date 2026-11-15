# Copilot instructions for this repository

This repository is a collection of small Python exercise projects grouped by week (`viikko1`, `viikko2`, `viikko3`). There is no single root application or shared build pipeline; each project is self-contained and should be treated as its own app.

## Build, test, and lint commands

Run commands from the relevant project directory rather than the repo root.

### `viikko2/nhl-reader`

```bash
cd viikko2/nhl-reader
uv sync --group dev
uv run pytest
uv run pytest tests/test_player_stats.py -q
uv run pylint src
uv run ruff check .
```

This project is configured with `pytest` using `pythonpath = ["src"]` and `testpaths = ["tests"]`.

### `viikko3/login`

```bash
cd viikko3/login
uv sync --group dev
uv run python src/index.py
uv run robot --variable HEADLESS:true src/tests
uv run robot --variable HEADLESS:true src/tests/login.robot
```

The Robot tests target the Flask app over HTTP (`http://localhost:5001`). The app exposes a test reset endpoint (`POST /tests/reset`) to clear the in-memory user store between cases.

### `viikko3/hello-robot`

```bash
cd viikko3/hello-robot
uv sync --group dev
uv run robot src/tests/increase_counter.robot
```

## High-level architecture

- The repo is intentionally split by assignment and week, not by a single product architecture.
- `viikko3/login` is a small Flask application organized around the classic service/repository/entity split:
  - `src/app.py` contains the HTTP routes and request handling.
  - `src/services/user_service.py` validates input and enforces authentication/business rules.
  - `src/repositories/user_repository.py` stores users in memory.
  - `src/entities/user.py` defines the `User` model.
  - `src/templates/` holds the Jinja templates for login, registration, and welcome screens.
  - `src/AppLibrary.py` is the Robot library used by acceptance tests to drive the app from the browser/HTTP layer.
- `viikko2/nhl-reader` is a data/statistics application built around a reader abstraction and a statistics service:
  - `src/player_reader.py` and related readers fetch raw player data.
  - `src/player_stats.py` produces sorted and filtered statistics (team, nationality, goal scoring).
  - `tests/test_player_stats.py` uses stub readers to verify the calculations without real network/data files.
- There is no shared root package, no CI workflow at the repo root, and no single release build. Each project package is meant to be developed and validated independently.

## Key conventions

- Prefer `uv` and project-local environment files (`uv.lock`, `.python-version`, `.venv`) rather than global package installation.
- `pythonpath` and import conventions are project-specific. For example, `nhl-reader` tests import from `player_stats` directly because the `src` directory is on `PYTHONPATH` during pytest.
- In the login app, business rules and validations live in the service layer; the repository is deliberately simple and in-memory. Avoid introducing a database or global state unless the exercise explicitly calls for it.
- Robot acceptance tests in `viikko3/login` and `viikko3/hello-robot` are treated as the primary validation path; the app should be started before running them.
- Keep changes scoped to the specific exercise folder you are working on. This repo is educational and not organized as a single product monorepo.
