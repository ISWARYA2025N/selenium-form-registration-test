from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class ParabankFullTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
        self.driver.maximize_window()

    def test_register_and_login(self):
        driver = self.driver

        # Click Register
        driver.find_element(By.LINK_TEXT, "Register").click()

        # Fill the registration form
        driver.find_element(By.ID, "customer.firstName").send_keys("Iswarya")
        driver.find_element(By.ID, "customer.lastName").send_keys("N")
        driver.find_element(By.ID, "customer.address.street").send_keys("123 Main St")
        driver.find_element(By.ID, "customer.address.city").send_keys("Chennai")
        driver.find_element(By.ID, "customer.address.state").send_keys("TN")
        driver.find_element(By.ID, "customer.address.zipCode").send_keys("600001")
        driver.find_element(By.ID, "customer.phoneNumber").send_keys("9876543210")
        driver.find_element(By.ID, "customer.ssn").send_keys("123456789")

        # Unique username using timestamp
        username = "user" + str(int(time.time()))
        password = "Test@123"

        driver.find_element(By.ID, "customer.username").send_keys(username)
        driver.find_element(By.ID, "customer.password").send_keys(password)
        driver.find_element(By.ID, "repeatedPassword").send_keys(password)

        # Submit the form
        driver.find_element(By.CSS_SELECTOR, "input[value='Register']").click()
        time.sleep(30)

        # ✅ Verify registration
        success_msg = driver.find_element(By.CLASS_NAME, "title").text
        self.assertIn("Welcome", success_msg)
        print("Registration Successful!")

        # 🔁 Log out
        driver.find_element(By.LINK_TEXT, "Log Out").click()
        time.sleep(2)

        # 🔐 Log in with the same credentials
        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "input[value='Log In']").click()
        time.sleep(500)

        # ✅ Verify login
        account_overview = driver.find_element(By.LINK_TEXT, "Accounts Overview")
        self.assertTrue(account_overview.is_displayed())
        print("Login Successful!")

        # 📸 Take screenshot
        driver.save_screenshot("parabank_login_success.png")
        print("Screenshot saved: parabank_login_success.png")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

