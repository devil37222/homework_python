from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CalculatorPage import CalculatorPage
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

def test_result(driver):

    button_page = CalculatorPage(driver)
    return driver
   
    assert button_page
 
    driver.quit()