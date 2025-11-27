from playwright.sync_api import Locator
from pages.basepage import BasePage
class HomePage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self.logo="Website for automation practice"
    def checkVisibilityOfLogo(self)->Locator:
        element=self.page.get_by_alt_text(self.logo)
        return element