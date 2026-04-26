import pytest
import allure
from selenium import webdriver
from data.config import Config

@pytest.fixture(scope="function")
def init_driver():
    options = webdriver.ChromeOptions()
    if Config.HEADLESS_MODE:
        options.add_argument("--headless=new")
        print("Running in headless mode")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(Config.IMPLICIT_WAIT_TIMEOUT)
    driver.maximize_window()
    driver.get(Config.BASE_UI_URL)

    yield driver
    driver.quit()