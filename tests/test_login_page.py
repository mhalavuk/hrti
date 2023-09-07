from utils.driver_manager import AppiumDriverManager
from pages.page_factory import PageFactory
from locators.home_page_locators import HomePageLocators
from decouple import config

driver = AppiumDriverManager.get_driver()
page_factory = PageFactory(driver)


def test_successful_login():

    login_page = page_factory.get_login_page()
    login_page.enter_username(config("TEST_EMAIL"))
    login_page.enter_password(config("TEST_PASSWORD"))
    login_page.click_login()

    home_page = page_factory.get_home_page()
    # if strings match, login was successful
    assert (home_page.get_cover_item_poster() == HomePageLocators.COVER_ITEM_POSTER)
