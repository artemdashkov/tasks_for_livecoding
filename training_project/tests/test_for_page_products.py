import time


class TestPageProducts:

    def test_01(self, driver):
        driver.get("https://dzen.ru/")
        time.sleep(5)
