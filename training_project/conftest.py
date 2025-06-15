import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.page_load_strategy = "normal"

    driver_path = ChromeDriverManager().install()
    driver = webdriver.Chrome(
        service=ChromeService(driver_path),
        options=chrome_options
    )

    # Принудительное удаление информации о безголовом режиме из --user-agent - используется для обхода капчи
    user_agent = driver.execute_script("return navigator.userAgent;")
    user_agent = user_agent.replace("Headless", "")
    chrome_options.add_argument(f"--user-agent={user_agent}")
    driver = webdriver.Chrome(
        service=ChromeService(driver_path),
        options=chrome_options
    )

    yield driver
    driver.quit()
