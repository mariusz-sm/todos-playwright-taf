from playwright.sync_api import Locator

from pages.base_page import BasePage


class TodosPage(BasePage):
    PATH = "/todomvc"

    def _init_locators(self) -> None:
        self.new_todo_input: Locator = self.page.locator("input.new-todo")
        self.todo_list: Locator = self.page.locator("ul.todo-list")
        self.todo_items: Locator = self.page.locator("ul.todo-list li")
        self.footer: Locator = self.page.locator("footer.footer")
        self.items_left_count: Locator = self.page.locator("span.todo-count strong")

        self.filter_all: Locator = self.page.get_by_role("link", name="All")
        self.filter_active: Locator = self.page.get_by_role("link", name="Active")
        self.filter_completed: Locator = self.page.get_by_role("link", name="Completed")
        self.clear_completed_button: Locator = self.page.get_by_role(
            "button", name="Clear completed"
        )

    def add_todo(self, text: str) -> None:
        self.new_todo_input.fill(text)
        self.new_todo_input.press("Enter")

    def get_todo_item(self, text: str) -> Locator:
        return self.todo_items.filter(has_text=text)

    def complete_todo(self, text: str) -> None:
        item = self.get_todo_item(text)
        item.locator("input.toggle").click()

    def delete_todo(self, text: str) -> None:
        item = self.get_todo_item(text)
        item.hover()
        item.get_by_role("button").click()

    def get_visible_todo_texts(self) -> list[str]:
        return self.todo_items.all_inner_texts()

    def get_items_left_count(self) -> int:
        return int(self.items_left_count.inner_text())
