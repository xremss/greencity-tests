import allure
from data.config import Config
from src.pages.base_page import BasePage
import time


@allure.title("Test Sign Up Modal - Successful Sign Up")
@allure.description("Test the Sign Up functionality with valid credentials.")
@allure.tag("Sign Up", "Smoke", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
def test_signup_successfully(init_driver):
    # Generate unique email with timestamp
    unique_email = f"{Config.EMAIL.split('@')[0]}_{int(time.time())}@{Config.EMAIL.split('@')[1]}"
    
    with allure.step("Open the application and click on Sign Up button"):
        page = BasePage(init_driver)
        signup_modal = page.click_sign_up()
        assert signup_modal.wait_until_displayed(), "Sign Up modal is not displayed"
    with allure.step("Enter valid credentials and attempt to sign up"):
        signup_modal.enter_email(unique_email)
        signup_modal.enter_username(Config.USER_NAME)
        signup_modal.enter_password(Config.PASSWORD)
        signup_modal.enter_repeat_password(Config.PASSWORD)
        signup_modal.click_sign_up()
    with allure.step("Verify that the sign-up modal disappears after successful registration"):
        assert signup_modal.wait_until_it_disappears(timeout=Config.EXPLICIT_WAIT_TIMEOUT), "Sign Up modal should disappear after successful sign up"