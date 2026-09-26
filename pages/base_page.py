from playwright.sync_api import Page

class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def click(self, locator):
        locator.click()

    def fill(self, locator, value):
        locator.fill(value)

    def get_text(self, locator):
        return locator.inner_text()

    def wait_for(self, locator):
        locator.wait_for()