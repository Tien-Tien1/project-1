#code tinh gọn
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import pytest
from time import sleep
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
import tests.conftest as conftest 


class TestLogin:
    @pytest.mark.smoke
    def test_login(self,driver):
        login_page = LoginPage(driver)
        # login_page.do_login('Admin' , 'admin123')
        login_page.do_login(ConfigReader.get_username(), ConfigReader.get_password())
        sleep(5)
        assert driver.find_element(By.XPATH, "//h6").text == "Dashboard" 
           
    def test_login_fail_wrong_username(self,driver):
        login_page = LoginPage(driver)
        login_page.enter_username("a")
        login_page.enter_password(ConfigReader.get_password())
        login_page.do_login('a',ConfigReader.get_password())
        sleep(10)
        assert driver.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text == "Invalid credentials"

    def test_login_fail_wrong_password(self,driver):
        login_page = LoginPage(driver)
        login_page.enter_username(ConfigReader.get_username())
        login_page.enter_password('')
        login_page.do_login(ConfigReader.get_username(),'')
        sleep(5)
        assert driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']").text == "Required"
    
    def test_login_fail_empty(self, driver):
        login_page = LoginPage(driver)
        login_page.enter_username('')
        login_page.enter_password('')
        login_page.do_login('', '')
        sleep(5)
        assert driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']").text == "Required"  
    
    def test_login_fail_wrong_username_password(self, driver):
        login_page = LoginPage(driver)
        login_page.enter_username("wrong_username")
        login_page.enter_password("wrong_password")
        login_page.do_login("wrong_username", "wrong_password")
        sleep(5)
        assert driver.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text == "Invalid credentials"
        


    