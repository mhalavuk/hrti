from traceback import print_exc
from logging import debug
from appium import webdriver
from os import getcwd


class AppiumDriverManager:
    _driver = None
    _desired_caps = {}

    @classmethod
    def initialize_driver(cls):

        appium_server_url = 'http://localhost:4723'

        if cls._driver is None:
            cls._desired_caps['platformName'] = 'Android'
            cls._desired_caps['automationName'] = 'UiAutomator2'
            cls._desired_caps['deviceName'] = 'Xiaomi'
            cls._desired_caps['app'] = f'{getcwd()}\\apks\\hrti.apk'

        try:
            debug("Initialize Appium Driver..")
            cls._driver = webdriver.Remote(appium_server_url, cls._desired_caps)
            cls._driver.implicitly_wait(10)
            debug("Driver is initialized")
            cls._driver = cls._driver

        except Exception as e:
            print_exc()
            debug(f"Driver initialization failure. ABORT !!!! {e}")

    @classmethod
    def get_driver(cls):
        cls.initialize_driver()
        return cls._driver

    @classmethod
    def close_driver(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None
