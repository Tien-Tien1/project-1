#code tinh gọn
from selenium.webdriver.common.by import By
import pytest
from time import sleep
from pages.login_page import LoginPage

class TestLogin:
   def test_login(self,driver):
        login_page = LoginPage(driver)
        login_page.do_login('Admin' , 'admin123')
        sleep(5)
        assert driver.find_element(By.XPATH, "//h6").text == "Dashboard" 
          
       
     
# def do_login(username, password):
#     driver.find_element(self.username).send_keys(username)
#     driver.find_element(self.password).send_keys(password)
#     driver.find_element(self.Click_login_btn).click()
    # def test_login_pass(self, driver):
    #     login_page = LoginPage(driver)
    #     login_page.enter_username("Admin")
    #     login_page.enter_password("admin123")
    #     login_page.Click_login_button()
    # sleep(5)
    