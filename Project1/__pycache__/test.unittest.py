from selenium import webdriver
import time
import unittest

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path =r"C:/Users/G3NY/Documents/Selenium_Projects/Webdriver/geckodriver-v0.30.0-win64/geckodriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    
    def test_login_valid(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        time.sleep(2)
        self.driver.find_element_by_id("welcome").click()
        self.driver.find_element_by_link_text("Logout").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()
        print("Test completed")

if __name__ == "__main__":
    unittest.main()
