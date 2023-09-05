from pages.login_page import LoginPage
from pages.home_page import HomePage


class PageFactory:
    _instance = None

    def __new__(cls, driver):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.driver = driver
        return cls._instance

    def get_login_page(self):
        return LoginPage(self.driver)

    def get_home_page(self):
        return HomePage(self.driver)
