import re
from playwright.sync_api import expect
from pages.homepage import HomePage
from pages.productspage import ProductsPage
class Test_ProductsPage:
    def test_CheckVisibilityOfItemsList(self,page):
        home_page=HomePage(page)
        home_page.navigate()
        home_page.clickProductsPageLink()
        products_page=ProductsPage(page)
        expect(products_page.getFeaturesItemsLocator()).to_be_visible()