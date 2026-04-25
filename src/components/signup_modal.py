import allure
from selenium.webdriver.common.by import By
from src.components.base_component import BaseComponent
from selenium.webdriver.support import expected_conditions as EC


class SignupModal(BaseComponent):
    email = (By.ID, "email")
    first_name = (By.ID, "firstName")
    password = (By.ID, "password")
    repeat_password = (By.ID, "repeatPassword")
    sign_up_button = (By.XPATH, "//button[@type='submit']")
    sign_up_with_google_button = (By.CLASS_NAME, "google-sign-in")
    sign_in_button = (By.XPATH, '//a[contains(text(), "Sign in")]')
    close_button = (By.CLASS_NAME, "cross-btn")
    email_error = (By.ID, "email-err-msg")
    password_error = (By.ID, "pass-err-msg")

    @allure.step("Enter email: {email}")
    def enter_email(self, email):
        email_field = self.find_element(*self.email)
        email_field.clear()
        email_field.send_keys(email)

    @allure.step("Enter username: {first_name}")
    def enter_username(self, first_name):
        username_field = self.find_element(*self.first_name)
        username_field.clear()
        username_field.send_keys(first_name)

    @allure.step("Enter password")
    def enter_password(self, password):
        password_field = self.find_element(*self.password)
        password_field.clear()
        password_field.send_keys(password)

    @allure.step("Enter repeat password")
    def enter_repeat_password(self, repeat_password):
        repeat_password_field = self.find_element(*self.repeat_password)
        repeat_password_field.clear()
        repeat_password_field.send_keys(repeat_password)

    @allure.step("Click Forgot Password link")
    def click_forgot_password(self):
        forgot_password_link = self.find_element(*self.forgot_password)
        forgot_password_link.click()

    @allure.step("Click Sign Up button")
    def click_sign_up(self):
        sign_up_btn = self.find_element(*self.sign_up_button)
        sign_up_btn.click()

    @allure.step("wait until email is not displayed")
    def wait_until_it_disappears(self, timeout=1):
        try:
            self._get_wait(timeout).until(
                EC.invisibility_of_element_located(self.email)
            )
            return True
        except:
            return False

    @allure.step("wait until modal is displayed")
    def wait_until_displayed(self, timeout=1):
        try:
            self._get_wait(timeout).until(
                EC.visibility_of_element_located(self.email)
            )
            return True
        except:
            return False

    @allure.step("Check if Sign Up modal is displayed")
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