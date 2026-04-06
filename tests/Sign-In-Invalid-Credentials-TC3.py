import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"

#Не працює з WSL падає на пошуку сайн ін
# class AuthTests(unittest.TestCase):

#     def setUp(self):
#         options = Options()
#         options.add_argument("--headless=new")
#         options.add_argument("--no-sandbox")
#         options.add_argument("--disable-dev-shm-usage")

#         self.driver = webdriver.Chrome(options=options)
#         self.driver.maximize_window()
#         self.wait = WebDriverWait(self.driver, 10)
#         self.driver.get(BASE_URL)

#     def tearDown(self):
#         self.driver.quit()

#     def test_sign_in_invalid_credentials(self):
#         driver = self.driver
#         wait = self.wait

#         # Open Sign In
#         wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()=' Sign in ']"))).click()

#         # Fill form
#         wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys("test@gmail.com")
#         driver.find_element(By.ID, "password").send_keys("wrongPassword123")

#         # Submit
#         driver.find_element(By.XPATH, "//button[@class='greenStyle']").click()

#         # Assert error message
#         error_msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'alert-general-error')]")))

# if __name__ == "__main__":
#     unittest.main()

class AuthTests(unittest.TestCase):

    def setUp(self):
        # options = Options()
        # options.add_argument("--headless=new")
        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(BASE_URL)

    def tearDown(self):
        self.driver.quit()

    def test_sign_in_invalid_credentials(self):
        driver = self.driver
        wait = self.wait

        # Open Sign In
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()=' Sign in ']"))).click()

        # Fill form
        wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys("test@gmail.com")
        driver.find_element(By.ID, "password").send_keys("wrongPassword123")

        # Submit
        driver.find_element(By.XPATH, "//button[@class='greenStyle']").click()

        # Assert error message
        error_msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class,'alert-general-error')]")))

if __name__ == "__main__":
    unittest.main()