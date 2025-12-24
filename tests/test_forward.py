from selenium.webdriver.common.by import By
import pytest
from time import sleep
from selenium import webdriver
import time


def test_foward(driver):
    title = driver.title
    print(f"\n 1st is: {title}")
    time.sleep(2)
    driver.get("https://www.google.com/")
    title = driver.title
    print(f"2nd is: {title}")
    driver.back()
    time.sleep(2)
    title = driver.title
    print(f"3th is: {title}")
    driver.forward()
    print(f"4th is: {driver.title}")


