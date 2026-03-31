import allure
import pytest

from pages.todos_page import TodosPage

ACTIVE_ITEM = "Active item"
COMPLETED_ITEM = "Completed item"


@allure.feature("Filters")
class TestFilters:

    @pytest.fixture()
    def two_todos_one_completed(self, todos_page):
        todos_page.add_todo(ACTIVE_ITEM)
        todos_page.add_todo(COMPLETED_ITEM)
        todos_page.complete_todo(COMPLETED_ITEM)
        yield todos_page

    @allure.title("Active filter shows only incomplete todos")
    def test_active_filter_shows_only_incomplete_todos(
        self, two_todos_one_completed: TodosPage
    ) -> None:
        two_todos_one_completed.filter_active.click()

        assert two_todos_one_completed.get_todo_item(ACTIVE_ITEM).is_visible()
        assert not two_todos_one_completed.get_todo_item(COMPLETED_ITEM).is_visible()

    @allure.title("Completed filter shows only completed todos")
    def test_completed_filter_shows_only_completed_todos(
        self, two_todos_one_completed: TodosPage
    ) -> None:
        two_todos_one_completed.filter_completed.click()

        assert two_todos_one_completed.get_todo_item(COMPLETED_ITEM).is_visible()
        assert not two_todos_one_completed.get_todo_item(ACTIVE_ITEM).is_visible()
