from selenium.webdriver.common.by import By
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.cover_item_poster = (By.ID, HomePageLocators.COVER_ITEM_POSTER)

    def get_cover_item_poster(self):
        self.click_element(self.cover_item_poster)
        return HomePageLocators.COVER_ITEM_POSTER
