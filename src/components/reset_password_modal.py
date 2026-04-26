import allure
from selenium.webdriver.common.by import By
from .base_component import BaseComponent
from selenium.webdriver.support import expected_conditions as EC
from data.config import Config


class ResetPasswordModal(BaseComponent):

    email = (By.ID, "email")
    submit_button = (By.XPATH, "//button[@type='submit']")
    sign_in_with_google_button = (By.CLASS_NAME, "google-sign-in")
    back_to_signin_button = (By.XPATH, '//a[contains(text(), "Back to Sign in")]')
    close_button = (By.CLASS_NAME, "close-modal-window")
    email_error = (By.ID, "email-err-msg")

    @allure.step("Enter email: {email}")
    def enter_email(self, email):
        email_field = self.find_element(*self.email)
        email_field.clear()
        email_field.send_keys(email)

    @allure.step("Click Submit button")
    def click_submit(self):
        submit_btn = self.find_element(*self.submit_button)
        submit_btn.click()

    @allure.step("wait until modal is displayed")
    def wait_until_displayed(self, timeout=Config.EXPLICIT_WAIT_TIMEOUT):
        try:
            self._get_wait(timeout).until(
                EC.visibility_of_element_located(self.email)
            )
            return True
        except:
            return False

    @allure.step("wait until email is not displayed")
    def wait_until_it_disappears(self, timeout=Config.EXPLICIT_WAIT_TIMEOUT):
        try:
            self._get_wait(timeout).until(
                EC.invisibility_of_element_located(self.email)
            )
            return True
        except:
            return False

    @allure.step("Check if Reset Password modal is displayed")
    def is_displayed(self):
        return self.node.is_displayed()

    @allure.step("get email error message")
    def email_error_message(self):
        return self.find_element(*self.email_error).text

    @allure.step("get password error message")
    def password_error_message(self):
        return self.find_element(*self.password_error).text

    @allure.step("Check if email error message is displayed")
    def email_error_is_displayed(self):
        return self.find_element(*self.email_error).is_displayed()