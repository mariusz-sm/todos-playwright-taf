import pytest
from playwright.sync_api import Page

from pages.todos_page import TodosPage


@pytest.fixture()
def todos_page(page: Page) -> TodosPage:
    todos = TodosPage(page)
    todos.navigate()
    return todos
