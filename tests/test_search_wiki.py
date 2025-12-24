import pytest
from selenium import webdriver
import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from time import sleep

class TestSearchWiki:
    def ReadDataFromFile(file_path):
        with open(file_path, mode="r") as file:
            csv_reader = csv.DictReader(file)
            keywords = [] 
            for row in csv_reader:
                keywords.append(row["keyword"])
            return keywords
        
    testdata = ReadDataFromFile("data.csv")
    
    @pytest.mark.parametrize("keyword", testdata)
    def test_search_wikipedia1(self, driver, keyword): #đặt tên bắt đầu là test để pytest hổ trợ
        search_box = driver.find_element(By.NAME, "search")
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.ENTER)
        sleep(5)
