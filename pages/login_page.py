from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.username = (By.NAME , "username")
        self.password = (By.NAME , "password")
        self.Click_login_btn = (By.XPATH, "//button[@type='submit']")
        
    def enter_username(self, username):
        self.driver.find_element(*self.username).send_keys(username)
        # self.driver.find_element(By.NAME, "username").send_keys(username)
    
    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)
        # self.driver.find_element(By.NAME, "password").send_keys(password)   

    def Click_login_button(self):
        self.driver.find_element(*self.Click_login_btn).click()
        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click
    
    def do_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.Click_login_btn()
        
    def Get_error_message(self):
        return self.driver1.find_element(By.XPATH, "//p[@class= 'oxd-text oxd-text--p oxd-alert-content-text']").text