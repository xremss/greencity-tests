import allure

from selenium.webdriver.common.by import By
from time import sleep

from src.components.signup_modal import SignupModal

class BasePage:
    sign_in_button_locator = (By.CSS_SELECTOR, ".header_navigation-menu-right-list > .header_sign-in-link")
    sign_in_modal_locator = (By.XPATH, "//app-auth-modal")
    sign_up_button_locator = (By.CSS_SELECTOR, ".header_navigation-menu-right-list > .header_sign-up-link")
    sign_up_modal_locator = (By.XPATH, "//app-auth-modal")

    def __init__(self, driver):
        self.driver = driver
    
    # @allure.step("Get Sign In button")
    # def get_sign_in_button(self):
    #     return self.driver.find_element(*self.sign_in_button_locator)

    # @allure.step("Get Sign In modal")
    # def _get_sign_in_modal(self):
    #     return self.driver.find_element(*self.sign_in_modal_locator)
    
    # @allure.step("Click Sign In button")
    # def click_sign_in(self):
    #     sign_in_button = self.get_sign_in_button()
    #     sign_in_button.click()
    #     return SigninModal(self._get_sign_in_modal())
    
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