from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver

class TestAlert:
    def test_alert_accept(self, timeout=10):
        """Open practice page, click Alert, switch to popup and accept (OK)."""
        url = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()

        # click Alert button (try common ids then fallback)
        try:
            driver.find_element(By.ID, "alertbtn").click()
        except Exception:
            try:
                driver.find_element(By.ID, "alertButton").click()
            except Exception:
                driver.find_element(By.XPATH, "//button[contains(., 'Alert')]").click()
        sleep(5)
        # wait for the alert and accept it
        WebDriverWait(driver, timeout).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        