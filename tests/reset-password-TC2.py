import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"
class AuthTests(unittest.TestCase):
 # Не працює для WSL.Думав що проблема з тим,що відкриваєтся у неповноєкраному режимі,та ломаєтся дом дерево.Але ні
    # def setUp(self):
        # options = Options()
        # options.add_argument("--headless=new")
        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-dev-shm-usage")

        # self.driver = webdriver.Chrome(options=options)
        # self.driver.maximize_window()
        # self.wait = WebDriverWait(self.driver, 10)
        # self.driver.get(BASE_URL)

#     def tearDown(self):
#         self.driver.quit()

#     # Test Case 2: Reset Password
#     def test_reset_password(self):
#         driver = self.driver
#         wait = self.wait

#         # Open Forgot Password
#         wait.until(EC.element_to_be_clickable((By.XPATH, "//div/ul/img"))).click()
#         wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='forgot-password']"))).click()

#         # Enter email
#         wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys("xremsua+1@gmail.com")
#         driver.find_element(By.XPATH, "//button[@class='green-send-btn']").click()

#         # Assert reset email sent message
#         reset_msg = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".mat-mdc-snack-bar-label")))
#         self.assertTrue(reset_msg.is_displayed())

# if __name__ == "__main__":
#     unittest.main()

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(BASE_URL)

    def tearDown(self):
        self.driver.quit()

    # Test Case 2: Reset Password
    def test_reset_password(self):
        driver = self.driver
        wait = self.wait

        # Open Forgot Password
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()=' Sign in ']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='forgot-password']"))).click()

        # Enter email
        wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys("xremsua@gmail.com")
        driver.find_element(By.XPATH, "//button[@class='green-send-btn']").click()

        # Assert reset email sent message
        reset_msg = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".mat-mdc-snack-bar-label")))
        self.assertTrue(reset_msg.is_displayed())

if __name__ == "__main__":
    unittest.main()