from pages.todos_page import TodosPage


class TestDeleteTodo:

    def test_deleted_todo_does_not_appear_in_all_view(self, todos_page: TodosPage) -> None:
        todos_page.add_todo("To be deleted")
        todos_page.delete_todo("To be deleted")

        todos_page.filter_all.click()

        todo = todos_page.get_todo_item("To be deleted")
        assert not todo.is_visible(), "Deleted todo should not appear in All view"

    def test_deleted_todo_does_not_appear_in_active_view(self, todos_page: TodosPage) -> None:
        todos_page.add_todo("To be deleted")
        todos_page.delete_todo("To be deleted")

        todos_page.filter_active.click()

        todo = todos_page.get_todo_item("To be deleted")
        assert not todo.is_visible(), "Deleted todo should not appear in Active view"

    def test_deleted_todo_does_not_appear_in_completed_view(self, todos_page: TodosPage) -> None:
        todos_page.add_todo("To be deleted")
        todos_page.complete_todo("To be deleted")
        todos_page.delete_todo("To be deleted")

        todos_page.filter_completed.click()

        todo = todos_page.get_todo_item("To be deleted")
        assert not todo.is_visible(), "Deleted todo should not appear in Completed view"