from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver

class TestHover:
    def test_hover_main_item_2(self, timeout=10):
        """Open demoqa menu page, hover over 'Main Item 2' and sleep 10 seconds."""
        url = "https://demoqa.com/menu#"
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        
        wait = WebDriverWait(driver, timeout)
        elem = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Main Item 2']")))

        ActionChains(driver).move_to_element(elem).perform()
        # keep hovered for manual inspection
        sleep(5)
