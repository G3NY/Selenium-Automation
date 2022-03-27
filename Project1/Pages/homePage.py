import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".", "."))
from Project1.Locators.locators import locators

class HomePage():
    
    def __init__(self, driver):
        self.driver = driver     
        
    def click_welcome(self):
        self.driver.find_element_by_id(locators.welcome_link_id).click()
        
    def click_logout(self):
        self.driver.find_element_by_link_text(locators.logout_link_linkText).click()