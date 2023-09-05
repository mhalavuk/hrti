from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.username_input = (By.ID, LoginPageLocators.USERNAME_INPUT)
        self.password_input = (By.ID, LoginPageLocators.PASSWORD_INPUT)
        self.login_button = (By.ID, LoginPageLocators.LOGIN_BUTTON)

    def enter_username(self, username):
        self.send_keys_to_element(self.username_input, username)

    def enter_password(self, password):
        self.send_keys_to_element(self.password_input, password)

    def click_login(self):
        self.click_element(self.login_button)
