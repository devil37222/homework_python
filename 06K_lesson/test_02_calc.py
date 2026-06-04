from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


def test_fill_form():
    driver = webdriver.Edge()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    wait = driver.find_element(By.CSS_SELECTOR, "#delay")
    wait.clear()
    wait.send_keys(45)

    driver.find_element(By.XPATH, '//span[text()="7"]').click() 
    driver.find_element(By.XPATH, '//span[text()="+"]').click()
    driver.find_element(By.XPATH, '//span[text()="8"]').click()
    driver.find_element(By.XPATH, '//span[text()="="]').click()

    
    result = WebDriverWait(driver, 45).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div[class="screen"]'), "15"))
   
    assert result

    driver.quit()