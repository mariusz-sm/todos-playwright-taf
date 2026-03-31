import allure
import pytest

from pages.todos_page import TodosPage

TODO_TEXT = "To be deleted"


@allure.feature("Delete Todo")
class TestDeleteTodo:

    @pytest.fixture()
    def todo(self, todos_page):
        todos_page.add_todo(TODO_TEXT)
        yield todos_page

    @allure.title("Deleted todo does not appear in All view")
    def test_deleted_todo_does_not_appear_in_all_view(self, todo: TodosPage) -> None:
        todo.delete_todo(TODO_TEXT)

        todo.filter_all.click()

        assert not todo.get_todo_item(TODO_TEXT).is_visible()

    @allure.title("Deleted todo does not appear in Active view")
    def test_deleted_todo_does_not_appear_in_active_view(self, todo: TodosPage) -> None:
        todo.delete_todo(TODO_TEXT)

        todo.filter_active.click()

        assert not todo.get_todo_item(TODO_TEXT).is_visible()

    @allure.title("Deleted todo does not appear in Completed view")
    def test_deleted_todo_does_not_appear_in_completed_view(self, todo: TodosPage) -> None:
        todo.complete_todo(TODO_TEXT)
        todo.delete_todo(TODO_TEXT)

        todo.filter_completed.click()

        assert not todo.get_todo_item(TODO_TEXT).is_visible()
