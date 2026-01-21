import pytest
from selenium import webdriver
from utils.config_reader import ConfigReader

@pytest.fixture(scope="function") # Fixture for setting up and tearing down the WebDriver , neu dung sesson de bi loi
def driver():
    #day la phan setup drive cho cac test script dung va chi setup 1 lan duy nhat
    options = webdriver.ChromeOptions() # nếu dùng headless thì mở phần này lên
    options.add_argument("--headless=new") # nếu dùng headless thì mở phần này lên
    driver = webdriver.Chrome(options=options) # nếu dùng headless thì mở phần này lên
    # driver = webdriver.Chrome() #nếu dùng headless thì tắt phần này đi
    driver.implicitly_wait(10) # để tìm thấy 1 thành phần nào đó trong tối da 10s de drive co gan lam gì đó
    driver.maximize_window()
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    #base_url = "https://www.wikipedia.org"  #để test trang wiki
    # base_url = "https://www.letskodeit.com/practice"
    # base_url = ConfigReader.get_base_url() 
    # base_url = "https://the-internet.herokuapp.com/dropdown"
    # base_url = "https://the-internet.herokuapp.com/dropdown"
    driver.get(base_url)
    # driver.title
    
    
    # driver.get(url)   #để test trang wiki
    yield driver #duy tri de no chay khong bi tat
    #day la phan teardown cho moi test script
    driver.quit()