import pytest
from playwright.sync_api import sync_playwright
@pytest.fixture(scope="session")
def browser():
    """Fixture to set up the testing environment before any tests run. Then tear it down after all tests have completed."""
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        yield browser
        browser.close()
    
@pytest.fixture()
def page(browser):
    page=browser.new_page()
    yield page
    page.close()