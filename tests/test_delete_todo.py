import allure
import pytest

from pages.todos_page import TodosPage

ITEM_TO_DELETE = "To be deleted"
ITEM_TO_KEEP = "To keep"


@allure.feature("Delete Todo")
class TestDeleteTodo:

    @pytest.fixture()
    def two_todos(self, todos_page):
        todos_page.add_todo(ITEM_TO_DELETE)
        todos_page.add_todo(ITEM_TO_KEEP)
        yield todos_page

    @allure.title("Deleted todo does not appear in All view")
    def test_deleted_todo_does_not_appear_in_all_view(self, two_todos: TodosPage) -> None:
        two_todos.delete_todo(ITEM_TO_DELETE)

        two_todos.filter_all.click()

        assert not two_todos.get_todo_item(ITEM_TO_DELETE).is_visible()

    @allure.title("Deleted todo does not appear in Active view")
    def test_deleted_todo_does_not_appear_in_active_view(self, two_todos: TodosPage) -> None:
        two_todos.delete_todo(ITEM_TO_DELETE)

        two_todos.filter_active.click()

        assert not two_todos.get_todo_item(ITEM_TO_DELETE).is_visible()

    @allure.title("Deleted todo does not appear in Completed view")
    def test_deleted_todo_does_not_appear_in_completed_view(self, two_todos: TodosPage) -> None:
        two_todos.complete_todo(ITEM_TO_DELETE)
        two_todos.delete_todo(ITEM_TO_DELETE)

        two_todos.filter_completed.click()

        assert not two_todos.get_todo_item(ITEM_TO_DELETE).is_visible()

    @allure.title("Deleting all todos hides filters and shows only input")
    def test_deleting_all_todos_hides_filters(self, todos_page: TodosPage) -> None:
        todos_page.add_todo(ITEM_TO_DELETE)
        todos_page.delete_todo(ITEM_TO_DELETE)

        assert not todos_page.footer.is_visible()
        assert todos_page.new_todo_input.is_visible()
