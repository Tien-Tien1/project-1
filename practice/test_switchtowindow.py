from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep
from selenium import webdriver

class TestMaxSize:
    def test_switch_to_new_window_and_maximize(self, timeout=10):
        self.url = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(self.url)

        original = driver.current_window_handle

        # click Open Window (try id then fallback)
        # try:
        driver.find_element(By.ID, "openwindow").click()
        # except Exception:
            # driver.find_element(By.XPATH, "//button[contains(., 'Open Window')]").click()

        WebDriverWait(driver, timeout).until(EC.number_of_windows_to_be(2))

        # switch to the new window
        for h in driver.window_handles:
            if h != original:
                driver.switch_to.window(h)
                break

        driver.maximize_window()
        sleep(5)

        # cleanup: close new window and return
        driver.close()
        driver.switch_to.window(original)
