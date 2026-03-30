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
| [Poetry](https://python-poetry.org/) | Dependency management |

## Project Structure

```
todos-playwright-taf/
├── pages/
│   └── todos_page.py      # Page Object Model for the TodoMVC page
├── tests/
│   ├── conftest.py        # Shared fixtures (todos_page)
│   ├── test_add_todo.py
│   ├── test_complete_todo.py
│   ├── test_delete_todo.py
│   └── test_filters.py
└── pyproject.toml
```

The framework uses the **Page Object Model (POM)** pattern. `TodosPage` encapsulates all locators and actions, keeping tests clean and focused on behaviour.

## Setup

### Prerequisites

- Python 3.12+
- [Poetry](https://python-poetry.org/docs/#installation)

### Install

```bash
poetry install
poetry run playwright install
```

`poetry install` installs Python dependencies. `playwright install` downloads the browser binaries (Chromium, Firefox, WebKit) — this step is required and is separate from the Python package install.

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

Run in headed mode (visible browser):

```bash
poetry run pytest --headed
```

Run on a specific browser (default is Chromium):

```bash
poetry run pytest --browser firefox
poetry run pytest --browser webkit
```

## Test Overview

| File | Class | What it covers |
|---|---|---|
| `test_add_todo.py` | `TestAddTodo` | Adding todos: English text, non-English characters, numbers |
| `test_complete_todo.py` | `TestCompleteTodo` | Completing a todo: Completed view visibility, CSS class |
| `test_delete_todo.py` | `TestDeleteTodo` | Deleting todos: absence in All, Active, and Completed views |
| `test_filters.py` | `TestFilters` | Filter behaviour: Active and Completed filters |
