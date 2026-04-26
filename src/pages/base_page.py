import allure

from selenium.webdriver.common.by import By
from time import sleep

from src.components.signup_modal import SignupModal
from src.components.signin_modal import SigninModal
from src.components.reset_password_modal import ResetPasswordModal

class BasePage:
    sign_in_button_locator = (By.CSS_SELECTOR, ".header_navigation-menu-right-list > .header_sign-in-link")
    sign_in_modal_locator = (By.XPATH, "//app-auth-modal")
    sign_up_button_locator = (By.CSS_SELECTOR, ".header_navigation-menu-right-list > .header_sign-up-link")
    sign_up_modal_locator = (By.XPATH, "//app-auth-modal")
    reset_password_button_locator = (By.CSS_SELECTOR, ".header_navigation-menu-right-list > .header_reset-password-link")
    reset_password_modal_locator = (By.XPATH, "//app-auth-modal")

    def __init__(self, driver):
        self.driver = driver
    
    
    # Sign In methods
    @allure.step("Get Sign In button")
    def get_sign_in_button(self):
        return self.driver.find_element(*self.sign_in_button_locator)

    @allure.step("Get Sign In modal")
    def _get_sign_in_modal(self):
        return self.driver.find_element(*self.sign_in_modal_locator)
    
    @allure.step("Click Sign In button")
    def click_sign_in(self):
        sign_in_button = self.get_sign_in_button()
        sign_in_button.click()
        return SigninModal(self._get_sign_in_modal())
    
    # Sign Up methods
    @allure.step("Get Sign Up button")
    def get_sign_up_button(self):
        return self.driver.find_element(*self.sign_up_button_locator)

    @allure.step("Get Sign Up modal")
    def _get_sign_up_modal(self):
        return self.driver.find_element(*self.sign_up_modal_locator)
    
    @allure.step("Click Sign Up button")
    def click_sign_up(self):
        sign_up_button = self.get_sign_up_button()
        sign_up_button.click()
        return SignupModal(self._get_sign_up_modal())
    
    #Reset Password Modal
    @allure.step("Get Reset Password button")
    def get_reset_password_button(self):
        return self.driver.find_element(*self.reset_password_button_locator)

    @allure.step("Get Reset Password modal")
    def _get_reset_password_modal(self):
        return self.driver.find_element(*self.reset_password_modal_locator)
    
    @allure.step("Click Reset Password button")
    def click_reset_password(self):
        reset_password_button = self.get_reset_password_button()
        reset_password_button.click()
        return ResetPasswordModal(self._get_reset_password_modal())
    
    @allure.step("Click the Submit a login link button")
    def click_submit_login_link(self):
        submit_login_link = self.driver.find_element(By.XPATH, '//a[contains(text(), "Submit a login link")]')
        submit_login_link.click()
        return ResetPasswordModal(self._get_reset_password_modal())