from pages.basepage import BasePage
from playwright.sync_api import Locator
class ProductsPage(BasePage):
    def __init__(self, page) -> None:
        super().__init__(page)
        self.featuredItems="div.features_items"
    def navigate(self):
        self.page.goto("https://automationexercise.com/products")
    def getFeaturesItemsLocator(self)->Locator:
        element=self.page.locator(self.featuredItems)
        return element