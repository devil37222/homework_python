from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from MainShopPage import MainShopPage 
from CartPage import CartPage
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

def test_result(driver):
    main_page = MainShopPage(driver)
    cart_page = CartPage(driver)

    price = MainShopPage(driver)
    assert price