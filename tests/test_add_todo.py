import allure
import pytest

from pages.todos_page import TodosPage


@allure.feature("Add Todo")
class TestAddTodo:

    @allure.title("Add todo with various text types: {text}")
    @pytest.mark.parametrize(
        "text",
        [
            "Buy groceries",
            "Ćma",
            "Task 42",
        ],
    )
    def test_add_todo(self, todos_page: TodosPage, text: str) -> None:
        todos_page.add_todo(text)

        todo = todos_page.get_todo_item(text)
        assert todo.is_visible(), f"Todo '{text}' should be visible after adding"

    @allure.title("Add todo with English text")
    def test_add_todo_with_english_text(self, todos_page: TodosPage) -> None:
        todos_page.add_todo("Buy groceries")

        todo = todos_page.get_todo_item("Buy groceries")
        assert todo.is_visible(), "Todo with English text should be visible"

    @allure.title("Add todo with non-English characters")
    def test_add_todo_with_non_english_characters(self, todos_page: TodosPage) -> None:
        todos_page.add_todo("Ćma")

        todo = todos_page.get_todo_item("Ćma")
        assert todo.is_visible(), "Todo with non-English characters should be visible"

    @allure.title("Add todo containing numbers")
    def test_add_todo_with_numbers(self, todos_page: TodosPage) -> None:
        todos_page.add_todo("Task 42")

        todo = todos_page.get_todo_item("Task 42")
        assert todo.is_visible(), "Todo containing numbers should be visible"
