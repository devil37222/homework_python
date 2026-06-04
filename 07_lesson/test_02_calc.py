from selenium import webdriver
from CalculatorPage import CalculatorPage
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")


def test_result(driver):

    button_page = CalculatorPage(driver)
    return driver
    assert button_page
    driver.quit()
