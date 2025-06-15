from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver: Chrome = driver
        self.wait = WebDriverWait(self.driver, 5, poll_frequency=1)
