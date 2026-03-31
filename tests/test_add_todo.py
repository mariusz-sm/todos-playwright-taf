import allure
import pytest

from pages.todos_page import TodosPage


@allure.feature("Add Todo")
class TestAddTodo:

    @allure.title("Add todo: {text}")
    @pytest.mark.parametrize(
        "text",
        [
            pytest.param("Buy groceries", id="english_text", marks=pytest.mark.smoke),
            pytest.param("Ćma", id="non_english_characters"),
            pytest.param("Task 42", id="text_with_numbers"),
        ],
    )
    def test_add_todo(self, todos_page: TodosPage, text: str) -> None:
        todos_page.add_todo(text)

        todo = todos_page.get_todo_item(text)
        assert todo.is_visible(), f"Todo '{text}' should be visible after adding"
