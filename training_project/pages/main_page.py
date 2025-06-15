import time
from datetime import datetime
from training_project.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    URL = "https://dzen.ru/"
    BUTTON_FIND = (By.CSS_SELECTOR, '.arrow__button[type="submit"]')
    SEARCH_FIELD = (By.XPATH, '//input[@class="arrow__input mini-suggest__input"]')
    FRAME = (By.CSS_SELECTOR, '[id*="ya-search-iframe"]')
    FIRST_STRING = (By.XPATH, "//h2[1]")

    def get_page(self):
        self.driver.get(self.URL)
        current_page = self.driver.current_url
        time.sleep(3)
        assert  current_page == self.URL, f"Expected page don't opened. Current page is {current_page}"

    def put_message(self, message):
        print(f"{datetime.now()}\t start put_message")
        iframe = self.driver.find_element(*self.FRAME)
        self.driver.switch_to.frame(iframe)
        search_field = self.wait.until(EC.element_to_be_clickable(self.SEARCH_FIELD))
        search_field.click()
        search_field.send_keys(message)
        search_field.click()
        print(f"{datetime.now()}\t end put_message")

    def click_button_find(self):
        print(f"{datetime.now()}\t start click_button_find")
        # button_find = self.wait.until(EC.element_to_be_clickable(self.BUTTON_FIND))
        button_find = self.driver.find_element(*self.BUTTON_FIND)
        button_find.click()
        print(f"{datetime.now()}\t end click_button_find")

    def get_text_first_string(self):
        first_string = self.wait.until(EC.visibility_of_element_located(self.FIRST_STRING))
        text_first_string = first_string.text
        print(text_first_string)

    def close_active_tab(self):
        self.driver.close()
