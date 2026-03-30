from abc import ABC, abstractmethod

from playwright.sync_api import Page


class BasePage(ABC):
    PATH: str

    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url
        self._init_locators()

    @abstractmethod
    def _init_locators(self) -> None: ...

    def navigate(self) -> None:
        self.page.goto(self.base_url + self.PATH)
