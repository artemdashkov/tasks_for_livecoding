import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def driver():
    driver_path = ChromeDriverManager().install()
    driver = webdriver.Chrome(service=ChromeService(driver_path))
    yield driver
    driver.quit()
