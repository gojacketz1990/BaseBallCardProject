from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import configparser

def test_simplepage():
    driver = webdriver.Chrome()

    driver.get("http://www.google.com")


    searchText = driver.find_element(By.NAME, "q")
    searchText.send_keys("steak")


    wait = WebDriverWait(driver,10)

    searchButton = wait.until(EC.element_to_be_clickable((By.NAME,'btnK')))

    searchButton.click()

    time.sleep(5)
