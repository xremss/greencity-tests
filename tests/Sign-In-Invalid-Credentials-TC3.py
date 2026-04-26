import allure
from data.config import Config
from src.pages.base_page import BasePage

@allure.title("Test Sign In Modal - Failed Sign In")
@allure.description("Test the Sign In functionality with invalid credentials.")
@allure.tag("Sign In", "Smoke", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
def test_signin_with_invalid_credentials(init_driver):
    with allure.step("Open the application and click on Sign In button"):
        page = BasePage(init_driver)
        signin_modal = page.click_sign_in()
        assert signin_modal.wait_until_displayed(), "Sign In modal is not displayed"
    with allure.step("Enter invalid credentials and attempt to sign in"):
        signin_modal.enter_email(Config.INVALID_EMAIL)
        signin_modal.enter_password(Config.INVALID_PASSWORD)
        signin_modal.click_sign_in()
    with allure.step("Verify that the sign-in modal remains displayed and shows error messages"):
        assert signin_modal.email_error_is_displayed(), "Sign In modal should display email error message for invalid email"
        # assert signin_modal.password_error_is_displayed(), "Sign In modal should display password error message for invalid password"
        # Add assertions to check for specific error messages if applicable