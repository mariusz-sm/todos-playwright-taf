import allure

from pages.todos_page import TodosPage


@allure.feature("Filters")
class TestFilters:

    @allure.title("Active filter shows only incomplete todos")
    def test_active_filter_shows_only_incomplete_todos(self, todos_page: TodosPage) -> None:
        todos_page.add_todo("Active item")
        todos_page.add_todo("Completed item")
        todos_page.complete_todo("Completed item")

        todos_page.filter_active.click()

        assert todos_page.get_todo_item(
            "Active item"
        ).is_visible(), "Active item should be visible in Active view"
        assert not todos_page.get_todo_item(
            "Completed item"
        ).is_visible(), "Completed item should not appear in Active view"

    @allure.title("Completed filter shows only completed todos")
    def test_completed_filter_shows_only_completed_todos(self, todos_page: TodosPage) -> None:
        todos_page.add_todo("Active item")
        todos_page.add_todo("Completed item")
        todos_page.complete_todo("Completed item")

        todos_page.filter_completed.click()

        assert todos_page.get_todo_item(
            "Completed item"
        ).is_visible(), "Completed item should be visible in Completed view"
        assert not todos_page.get_todo_item(
            "Active item"
        ).is_visible(), "Active item should not appear in Completed view"
