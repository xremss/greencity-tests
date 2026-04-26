import allure
from selenium.webdriver.common.by import By
from .base_component import BaseComponent
from selenium.webdriver.support import expected_conditions as EC
from data.config import Config

class SigninModal(BaseComponent):

    email = (By.ID, "email")
    password = (By.ID, "password")
    forgot_password = (By.CLASS_NAME, "forgot-password")
    sign_in_button = (By.XPATH, "//app-sign-in//button[@type='submit']")
    sign_in_with_google_button = (By.CLASS_NAME, "google-sign-in")
    sign_up_button = (By.XPATH, '//a[contains(text(), "Sign up")]')
    close_button = (By.CLASS_NAME, "close-modal-window")
    email_error = (By.ID, "email-err-msg")
    password_error = (By.ID, "pass-err-msg")

    @allure.step("Enter email: {email}")
    def enter_email(self, email):
        email_field = self.find_element(*self.email)
        email_field.clear()
        email_field.send_keys(email)

    @allure.step("Enter password")
    def enter_password(self, password):
        password_field = self.find_element(*self.password)
        password_field.clear()
        password_field.send_keys(password)

    @allure.step("Click Forgot Password link")
    def click_forgot_password(self):
        forgot_password_link = self.find_element(*self.forgot_password)
        forgot_password_link.click()

    @allure.step("Click Sign In button")
    def click_sign_in(self):
        sign_in_btn = self.find_element(*self.sign_in_button)
        sign_in_btn.click()

    @allure.step("wait until email is not displayed")
    def wait_until_it_disappears(self, timeout=Config.EXPLICIT_WAIT_TIMEOUT):
        try:
            self._get_wait(timeout).until(
                EC.invisibility_of_element_located(self.email)
            )
            return True
        except:
            return False

    @allure.step("wait until modal is displayed")
    def wait_until_displayed(self, timeout=Config.EXPLICIT_WAIT_TIMEOUT):
        try:
            self._get_wait(timeout).until(
                EC.visibility_of_element_located(self.email)
            )
            return True
        except:
            return False

    @allure.step("Check if Sign In modal is displayed")
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
    
    @allure.step("Check if password error message is displayed")
    def password_error_is_displayed(self):
        return self.find_element(*self.password_error).is_displayed()