class BasePage:
    def __init__(self,page) -> None:
        self.page=page
    def navigate(self):
        self.page.goto("https://automationexercise.com/")
    def getTitle(self)->str:
        title= self.page.title()
        return title