import allure
import pytest

from pages.todos_page import TodosPage

TODO_TEXT = "Complete todo"


@allure.feature("Complete Todo")
class TestCompleteTodo:

    @pytest.fixture()
    def completed_todo(self, todos_page):
        todos_page.add_todo(TODO_TEXT)
        todos_page.complete_todo(TODO_TEXT)
        yield todos_page

    @allure.title("Todo item can be marked as completed")
    def test_todo_item_can_be_marked_as_completed(self, completed_todo: TodosPage) -> None:
        todo = completed_todo.get_todo_item(TODO_TEXT)

        assert "completed" in todo.get_attribute("class")

    @allure.title("Completed item appears in Completed view")
    def test_completed_item_appears_in_completed_view(self, completed_todo: TodosPage) -> None:
        completed_todo.filter_completed.click()

        assert completed_todo.get_todo_item(TODO_TEXT).is_visible()
