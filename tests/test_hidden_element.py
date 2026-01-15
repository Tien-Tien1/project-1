from selenium.webdriver.common.by import By
import pytest
from time import sleep
from selenium import webdriver
import time


def test_hidden_element(driver):
    hidden_button = driver.find_element(By.ID, "hide-textbox")
    hidden_button.click()
    sleep(2)
    #javascript
    find_textbox = driver.find_element(By.ID, "displayed-text")
    driver.execute_script("arguments[0].value = 'Merry Chrismas I wish all happy'", find_textbox) #arguments[0] la tham so truyen vao
    print('value:', find_textbox.get_attribute("value"))
    sleep(2)
    show_button = driver.find_element(By.ID, "show-textbox")
    show_button.click()
    sleep(2)
    assert find_textbox.get_attribute("value") == "Merry Chrismas I wish all happy"