#code tinh gọn
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
import tests.conftest as conftest 


class TestLogin:
   def test_login(self,driver: WebDriver):
        login_page = LoginPage(driver)
        # login_page.do_login('Admin' , 'admin123')
        login_page.do_login(ConfigReader.get_username(), ConfigReader.get_password())
        sleep(5)
        assert driver.find_element(By.XPATH, "//h6").text == "Dashboard" 
          
# class testloginfail:     
#     def test_login_fail_wrong_password(self,driver: WebDriver):
#         login_page = LoginPage(driver)
#         login_page.enter_username("")
#         login_page.enter_password(ConfigReader.get_password())
#         login_page.Click_login_button()
#         sleep(5)
#         assert driver.find_element(By.XPATH, "").text == ""
    
    # def test_login_fail_wrong_username(self,driver):
    #     login_page = LoginPage(driver)
    #     login_page.do_login("Admin1", "admin123")
    #     login_page.Click_login_button()
    #     assert driver.find_element(By.CSS_SELECTOR, ".oxd-text--h6").text == "Dashboard"
    #     sleep(5)
    
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
