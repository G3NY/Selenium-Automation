from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Project1.Pages.loginPage import LoginPage
from Project1.Pages.homePage import HomePage
import HtmlTestRunner

class LoginTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path =r"C:/Users/G3NY/Documents/Selenium_Projects/Webdriver/geckodriver-v0.30.0-win64/geckodriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    
    def test_login_valid(self):
        driver = self.driver
        
        driver.get("https://opensource-demo.orangehrmlive.com/")
        
        #so you don't have to keep using self.login
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        
        time.sleep(2)
        
        home = HomePage(driver)
        home.click_welcome()
        home.click_logout()

        time.sleep(2)

    def test_login_valid_2(self):
        driver = self.driver
        
        driver.get("https://opensource-demo.orangehrmlive.com/")
        
        #so you don't have to keep using self.login
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        
        time.sleep(2)
        
        home = HomePage(driver)
        home.click_welcome()
        home.click_logout()

        time.sleep(2)

    def test_login_valid_3(self):
        driver = self.driver
        
        driver.get("https://opensource-demo.orangehrmlive.com/")
        
        #so you don't have to keep using self.login
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        
        time.sleep(2)
        
        home = HomePage(driver)
        home.click_welcome()
        home.click_logout()

        time.sleep(2)
        
    @classmethod
    def tearDownClass(self):
        self.driver.close()
        self.driver.quit()
        print("Test completed")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r"C:/Users/G3NY/Documents/Selenium_Projects/Project1/reports"))