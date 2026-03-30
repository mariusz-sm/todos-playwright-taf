from pages.todos_page import TodosPage


class TestCompleteTodo:

    def test_completed_todo_appears_in_completed_view(self, todos_page: TodosPage) -> None:
        todos_page.add_todo("Buy milk")
        todos_page.complete_todo("Buy milk")

        todos_page.filter_completed.click()

        todo = todos_page.get_todo_item("Buy milk")
        assert todo.is_visible(), "Completed todo should appear in Completed view"

    def test_completed_todo_has_completed_css_class(self, todos_page: TodosPage) -> None:
        todos_page.add_todo("Buy milk")
        todos_page.complete_todo("Buy milk")

        todo = todos_page.get_todo_item("Buy milk")
        assert "completed" in todo.get_attribute("class"), \
            "Completed todo item should have 'completed' CSS class"