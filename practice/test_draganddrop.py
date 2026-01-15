from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
import pytest


class TestDragAndDrop:
    def test_drag_and_drop(self, timeout=15):
        url = "https://demo.guru99.com/test/drag_drop.html"
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        # driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))
        wait = WebDriverWait(driver, 15)
        drag = driver.find_element(By.ID, "fourth")
        drop = driver.find_element(By.ID, "shoppingCart4")
        
        actions = ActionChains(driver)
        actions.drag_and_drop(drag, drop).perform()
        
        sleep(10)  # Just to visually confirm the action during testing

        # assert drop.text == "Dropped!"