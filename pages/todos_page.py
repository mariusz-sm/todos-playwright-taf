from playwright.sync_api import Page, Locator


class TodosPage:
    URL = "https://demo.playwright.dev/todomvc"

    def __init__(self, page: Page) -> None:
        self.page = page

        self.new_todo_input: Locator = page.locator("input.new-todo")
        self.todo_list: Locator = page.locator("ul.todo-list")
        self.todo_items: Locator = page.locator("ul.todo-list li")
        self.footer: Locator = page.locator("footer.footer")
        self.items_left_count: Locator = page.locator("span.todo-count strong")

        self.filter_all: Locator = page.get_by_role("link", name="All")
        self.filter_active: Locator = page.get_by_role("link", name="Active")
        self.filter_completed: Locator = page.get_by_role("link", name="Completed")
        self.clear_completed_button: Locator = page.get_by_role("button", name="Clear completed")

    def navigate(self) -> None:
        self.page.goto(self.URL)

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