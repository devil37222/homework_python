from selenium import webdriver
from CalculatorPage import CalculatorPage
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver


def test_result(driver):
    button_page = CalculatorPage(driver)
    button_page.delay()
    button_page.button_number()
    button_page.get_search_results()
    assert button_page
    driver.quit()
