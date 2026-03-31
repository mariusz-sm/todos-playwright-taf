# Todos Playwright TAF

Test automation framework for the [TodoMVC](https://demo.playwright.dev/todomvc) demo app, built with Python, Pytest, and Playwright.

## Purpose

Validates core functionality of the TodoMVC application:

- Adding todos (including non-English characters and numeric content)
- Completing todos and verifying their state
- Deleting todos across all filter views
- Filtering todos by All / Active / Completed

## Tech Stack

| Tool | Role |
|---|---|
| [Python 3.12+](https://www.python.org/) | Language |
| [Pytest](https://docs.pytest.org/) | Test runner |
| [Playwright](https://playwright.dev/python/) | Browser automation |
| [pytest-playwright](https://playwright.dev/python/docs/test-runners) | Pytest integration |
| [pytest-xdist](https://pytest-xdist.readthedocs.io/) | Parallel test execution |
| [Allure](https://allurereport.org/) | Test reporting |
| [Poetry](https://python-poetry.org/) | Dependency management |

## Project Structure

```
todos-playwright-taf/
├── pages/
│   ├── base_page.py       # Abstract base class with shared locators and helpers
│   └── todos_page.py      # Page Object Model for the TodoMVC page
├── tests/
│   ├── conftest.py        # Shared fixtures (todos_page, screenshot on failure)
│   ├── test_add_todo.py
│   ├── test_complete_todo.py
│   ├── test_delete_todo.py
│   └── test_filters.py
├── pyproject.toml
└── pytest.ini
```

The framework uses the **Page Object Model (POM)** pattern. `TodosPage` encapsulates all locators and actions, keeping tests clean and focused on behaviour.

## Setup

### Prerequisites

Install the following before cloning the repository:

| Tool | Min version | Install guide |
|---|---|---|
| Python | 3.12 | [python.org](https://www.python.org/downloads/) |
| Poetry | any | [python-poetry.org](https://python-poetry.org/docs/#installation) |
| Allure CLI | any | [allurereport.org](https://allurereport.org/docs/v2/install-for-windows/) |

Verify your Python version:

```bash
python --version   # must be 3.12 or higher
```

> If you need to manage multiple Python versions, [pyenv](https://github.com/pyenv/pyenv) is a good option.

### Step 1 — Clone and install dependencies

```bash
git clone <repository-url>
cd todos-playwright-taf
poetry install
poetry run playwright install
```

`poetry install` installs all Python dependencies into an isolated virtual environment. `playwright install` downloads the browser binaries (Chromium, Firefox, WebKit) — this is a separate step and is required.

### Step 2 — Create pytest.ini

`pytest.ini` is not committed to the repository. You must create it in the project root before running tests.

Minimum required configuration:

```ini
[pytest]
testpaths = tests
pythonpath = .
addopts = --alluredir=allure-results -n 1
base_url = https://demo.playwright.dev
```

`base_url` is required — tests will fail without it. Set it to the base URL of the application under test.

See the [pytest.ini](#pytestini) section for other options.

### Step 3 — Verify the setup

Run the full test suite to confirm everything is working:

```bash
poetry run pytest
```

## Running Tests

Run all tests:

```bash
poetry run pytest
```

Run a specific test file:

```bash
poetry run pytest tests/test_add_todo.py
```

Run a specific test:

```bash
poetry run pytest tests/test_add_todo.py::TestAddTodo::test_add_todo
```

### Headed mode

By default, Playwright runs tests headlessly (no visible browser window). To run with a visible browser:

```bash
poetry run pytest --headed
```

### Browsers

The default browser is Chromium. To run on a different browser:

```bash
poetry run pytest --browser firefox
poetry run pytest --browser webkit
```

All three browsers (Chromium, Firefox, WebKit) are installed by `playwright install`.

### Device emulation

Playwright can emulate specific devices (screen size, user agent, touch support). To run tests against a specific device:

```bash
poetry run pytest --device "iPhone 13"
poetry run pytest --device "iPad Pro 11"
poetry run pytest --device "Pixel 5"
```

You can combine `--browser` and `--device`:

```bash
poetry run pytest --browser webkit --device "iPhone 13"
```

### Smoke tests

Smoke tests cover the three core user actions (add, complete, delete) and are meant for a quick sanity check — for example after a deployment.

```bash
poetry run pytest -m smoke        # run only smoke tests
```

```bash
poetry run pytest -m "not smoke"  # run everything except smoke tests
```

### Parallel execution

Tests run with a single worker by default (`-n 1` in `pytest.ini`). With ~11 tests, each worker spawns its own browser process and the startup overhead outweighs the time saved. Increase workers as the suite grows — at around 50+ tests the gains become meaningful.

```bash
poetry run pytest -n auto   # workers based on available CPU cores
poetry run pytest -n 4      # fixed number of workers
```

## pytest.ini

The `pytest.ini` file at the project root controls default options. Below is an annotated example:

```ini
[pytest]
testpaths = tests           # directory pytest collects tests from
pythonpath = .              # adds project root to sys.path (needed for 'pages' imports)
addopts =
    --alluredir=allure-results  # write Allure results to this directory
    -n 1                        # number of parallel workers (1 = sequential)
    # --headed                  # uncomment to always run with a visible browser
    # --browser firefox         # uncomment to change the default browser
    # --device "iPhone 13"      # uncomment to enable device emulation
base_url = https://demo.playwright.dev
markers =
    smoke: marks tests as smoke tests (fast, core user flows only)

Any option set in `addopts` applies to every `pytest` run. CLI flags passed at runtime override or extend `addopts`.

## Allure Report

Tests are annotated with `@allure.feature` and `@allure.title` for structured reporting. On failure, a screenshot is automatically captured and attached to the report.

### Generate and open report

**Step 1** — run tests (allure results are written to `allure-results/` automatically):

```bash
poetry run pytest
```

**Step 2** — generate and open the HTML report:

```bash
allure serve allure-results
```

`allure serve` generates the report and opens it in the browser in one step. Alternatively, to generate a static report:

```bash
allure generate allure-results --clean -o allure-report
allure open allure-report
```

## Test Overview

| File | Class | What it covers |
|---|---|---|
| `test_add_todo.py` | `TestAddTodo` | Adding todos: English text, non-English characters, numbers |
| `test_complete_todo.py` | `TestCompleteTodo` | Completing a todo: Completed view visibility, CSS class |
| `test_delete_todo.py` | `TestDeleteTodo` | Deleting todos: absence in All, Active, and Completed views |
| `test_filters.py` | `TestFilters` | Filter behaviour: Active and Completed filters |
