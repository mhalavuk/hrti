from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def wait_for_element_to_be_visible(self, by_locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(by_locator))
            return element
        except TimeoutException:
            raise NoSuchElementException(f"Element not found: {by_locator}")

    def click_element(self, by_locator):
        element = self.wait_for_element_to_be_visible(by_locator)
        element.click()

    def send_keys_to_element(self, by_locator, text):
        element = self.wait_for_element_to_be_visible(by_locator)
        element.clear()
        element.send_keys(text)
