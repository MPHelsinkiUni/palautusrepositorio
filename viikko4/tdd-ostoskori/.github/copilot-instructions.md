# Repository guidance

## Build and test commands

Run all commands from this project directory.

```bash
uv sync --group dev
uv run pytest
```

Run only the shopping-basket test module:

```bash
uv run pytest src/tests/ostoskori_test.py -q
```

Run one test by its unittest/pytest node ID:

```bash
uv run pytest src/tests/ostoskori_test.py::TestOstoskori::test_ostoskorin_hinta_ja_tavaroiden_maara_alussa -q
```

The project uses Python 3.14 and declares pytest as a development dependency. There is no configured linter or separate build step.

## Architecture

This is a small TDD exercise for implementing a shopping basket. The domain classes are in `src/`:

- `Tuote` identifies a product and stores its name and unit price.
- `Ostos` represents a basket line for one `Tuote`, including the line quantity and line total.
- `Ostoskori` is the basket API to implement. It exposes item count, total price, add/remove/clear operations, and basket contents.
- `src/index.py` is currently a placeholder for ad hoc test code.

The implementation is unfinished: several `OstosKori` methods are stubs. Tests under `src/tests/` define the required behavior and should drive incremental implementation.

## Conventions

- Use `uv run` for Python and pytest commands so they use the project-local `.venv` and Python 3.14 environment.
- Keep product, basket-line, and basket responsibilities separate across `Tuote`, `Ostos`, and `OstosKori`.
- Preserve the existing public method names and return shapes when implementing the stubs.
- Tests are written with `unittest.TestCase`; pytest discovers and runs them without a separate test runner.
- Module imports use bare local module names such as `from ostoskori import Ostoskori` and `from tuote import Tuote`; run tests from the project root as configured.
- Code of ostos.py and tuote.py should not be changed
- Tests should not be edited unless explicitly asked
- Always implement absolutely minimal code that makes the tests pass and only the tests. Do not implement features outside of the tests. Development is test-driven.