import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    #day la phan setup drive cho cac test script dung va chi setup 1 lan duy nhat
    driver = webdriver.Chrome()
    driver.implicitly_wait(10) # để tìm thấy 1 thành phần nào đó trong tối da 10s de drive co gan lam gì đó
    driver.maximize_window()
    # base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    #base_url = "https://www.wikipedia.org"  #để test trang wiki
    base_url = "https://www.letskodeit.com/practice"
    driver.get(base_url)
    # driver.title
    
    
    # driver.get(url)   #để test trang wiki
    yield driver #duy tri de no chay khong bi tat
    #day la phan teardown cho moi test script
    driver.quit()