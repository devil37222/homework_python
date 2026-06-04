from selenium import webdriver

from MainShopPage import MainShopPage
from CartPage import CartPage
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")


def test_result(driver):
    MainShopPage(driver)
    CartPage(driver)
    price = MainShopPage(driver)
    assert price
