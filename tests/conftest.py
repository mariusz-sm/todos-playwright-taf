import allure
import pytest
from playwright.sync_api import Page

from pages.todos_page import TodosPage


@pytest.fixture()
def todos_page(page: Page, base_url: str) -> TodosPage:
    todos = TodosPage(page, base_url)
    todos.navigate()
    return todos


@pytest.fixture(autouse=True)
def screenshot_on_failure(page: Page, request: pytest.FixtureRequest) -> None:
    yield
    if request.node.rep_call.failed:
        screenshot = page.screenshot()
        allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo) -> None:
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
