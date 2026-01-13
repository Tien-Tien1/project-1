from selenium.webdriver.common.by import By
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSubmit:
    def test_submit(self, driver):
        driver.get("https://the-internet.herokuapp.com/login")
        
        wait = WebDriverWait(driver, 10)
        
        user = driver.find_element(By.ID, "username")
        user.send_keys("tomsmith")

        pwd = driver.find_element(By.ID, "password")
        pwd.send_keys("SuperSecretPassword!")

        # submit form bằng submit() trên input password
        pwd.submit()

        flash = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "flash"))
        )
        assert "You logged into a secure area!" in flash.text