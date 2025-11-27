from playwright.sync_api import expect
import pytest 
import re
def test_sample(page):
    page.goto("https://automationexercise.com/")
    expect(page).to_have_title(re.compile("Automation Exercise"))