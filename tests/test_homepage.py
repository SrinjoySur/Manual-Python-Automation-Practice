import re
from playwright.sync_api import expect
from pages.homepage import HomePage
from pages.productspage import ProductsPage
class Test_HomePage_tests:
    def test_logoVisibility(self,page):
        home_page=HomePage(page)
        home_page.navigate()
        element=home_page.getLogoLocator()
        try:
            expect(element).to_be_visible()
        except:
            TimeoutError()
    def test_navigateToProductsPage(self,page):
        home_page=HomePage(page)
        home_page.navigate()
        home_page.clickProductsPageLink()
        products_page=ProductsPage(page)
        title=products_page.getTitle()
        assert re.search("Automation Exercise - All Products",title)