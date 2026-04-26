import allure
from data.config import Config
from src.pages.base_page import BasePage
from src.components.reset_password_modal import ResetPasswordModal



@allure.title("Test Reset Password - Successful Reset")
@allure.description("Test the reset password functionality with valid email.")
@allure.tag("Reset Password", "Smoke", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
def test_reset_password_successfully(init_driver):
    with allure.step("Open the application and click on Sign In button"):
        page = BasePage(init_driver)
        signin_modal = page.click_sign_in()
        assert signin_modal.wait_until_displayed(), "Sign In modal is not displayed"
    with allure.step("Click on Forgot Password link"):
        signin_modal.click_forgot_password()
        reset_modal = ResetPasswordModal(page._get_reset_password_modal())
        assert reset_modal.wait_until_displayed(), "Reset Password modal is not displayed"
    with allure.step("Enter valid email and attempt to reset password"):
        reset_modal.enter_email(Config.EMAIL)
    with allure.step("Click Submit button"):
        reset_modal.click_submit()
    with allure.step("Verify reset password success (e.g., success message or modal disappears)"):
        # Add appropriate assertion here, e.g., check for success message
        # For now, assuming the modal disappears on success
        assert reset_modal.wait_until_it_disappears(timeout=Config.EXPLICIT_WAIT_TIMEOUT), "Reset Password modal should disappear after successful reset"
