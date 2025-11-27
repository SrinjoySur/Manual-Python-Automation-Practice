from playwright.sync_api import Locator
class HomePage:
    def __init__(self,page):
        self.page=page
        self.logo="Website for automation practice"
    def navigate(self):
        self.page.goto("https://automationexercise.com/")
    def checkVisibilityOfLogo(self)->Locator:
        element=self.page.get_by_alt_text(self.logo)
        return element