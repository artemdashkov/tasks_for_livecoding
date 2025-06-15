import time
import pytest
from training_project.pages.main_page import MainPage

class TestPageProducts:

    @pytest.mark.parametrize('message', ['Первое сообщение', 'Второе сообщение'])
    def test_find_option(self, driver, message):
        main_page_object = MainPage(driver)
        main_page_object.get_page()
        main_page_object.put_message(message)
        main_page_object.click_button_find()
        main_page_object.get_text_first_string()
