from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.logger import get_logger

class LoginPage(BasePage):

    def __init__(self, page: Page,base_url):
        super().__init__(page)
        self.base_url = base_url

        self.logger=get_logger(__name__)

        self.username = page.locator(
            "input[placeholder='info@gmail.com']"
        )

        self.password = page.locator(
            "input[placeholder='Enter your password']"
        )

        self.login_button = page.locator(
            "button[type='submit']"
        )
        self.heading = page.get_by_role(
            "heading", name="Dashboard", exact=True)

    def open(self):
         self.logger.info("Opening login page")

         self.page.goto(self.base_url)

    def login(self, username, password):

        self.logger.info("Entering username")

        self.fill(self.username, username)
        self.fill(self.password, password)
        self.click(self.login_button)

   