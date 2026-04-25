import pytest
import allure
from selenium import webdriver
from data.config import Config

@pytest.fixture(scope="function")
def init_driver():
    with allure.step("Initialize WebDriver and open the application"):
        options = webdriver.ChromeOptions()
        if Config.HEADLESS_MODE:
            options.add_argument("--headless=new")
            print("Running in headless mode")
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(Config.IMPLICIT_WAIT_TIMEOUT)
        driver.maximize_window()
    with allure.step(f"Navigate to the base URL: {Config.BASE_UI_URL}"):
        driver.get(Config.BASE_UI_URL)

    # after yield code will be executed as teardown
    yield driver
    # before yield code will be executed as setup
    with allure.step("Quit WebDriver"):
        driver.quit()