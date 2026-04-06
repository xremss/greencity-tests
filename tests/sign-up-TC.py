import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"  # replace with your URL

class AuthTests(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(BASE_URL)

    def tearDown(self):
        self.driver.quit()

    # Test Case 1: Successful Sign Up
    def test_successful_sign_up(self):
        driver = self.driver
        wait = self.wait

        # Open Sign Up popup
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='header_sign-up-btn']"))).click()

        # Fill form
        wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys("test1234qwer@gmail.com")
        driver.find_element(By.ID, "firstName").send_keys("testuser")
        driver.find_element(By.ID, "password").send_keys("12345678Qw!")
        driver.find_element(By.ID, "repeatPassword").send_keys("12345678Qw!")

        # Submit
        driver.find_element(By.XPATH, "//button[@class='greenStyle']").click()

        # Assert success message
        success_msg = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".mat-mdc-snack-bar-actions.mdc-snackbar__actions")))
        self.assertTrue(success_msg.is_displayed())

if __name__ == "__main__":
    unittest.main()