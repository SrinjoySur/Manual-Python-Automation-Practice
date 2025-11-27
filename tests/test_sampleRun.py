from playwright.sync_api import expect
from pages.basepage import BasePage
import re
class Test_Sample:
    def test_sample(self,page):
        base_page=BasePage(page)
        base_page.navigate()
        title=base_page.getTitle()
        assert re.search("Automation Exercise",title)