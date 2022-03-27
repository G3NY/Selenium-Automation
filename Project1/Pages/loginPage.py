import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".", ". "))
from Project1.Locators.locators import locators

class LoginPage():
    
    def __init__(self, driver):
        self.driver = driver
          
    def enter_username(self, username):
        self.driver.find_element_by_id(locators.username_textbox_id).clear()
        self.driver.find_element_by_id(locators.username_textbox_id).send_keys(username)
        
    def enter_password(self, password):
        self.driver.find_element_by_id(locators.password_textbox_id).clear()
        self.driver.find_element_by_id(locators.password_textbox_id).send_keys(password)
        
    def click_login(self):
        self.driver.find_element_by_id(locators.login_button).click()