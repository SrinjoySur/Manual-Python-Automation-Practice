import re
from playwright.sync_api import expect
from pages.homepage import HomePage
def test_logoVisibility(page):
    home_page=HomePage(page)
    home_page.navigate()
    element=home_page.getLogoLocator()
    try:
        expect(element).to_be_visible()
    except:
        TimeoutError()
