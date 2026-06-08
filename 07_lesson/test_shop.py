from selenium import webdriver
from MainShopPage import MainShopPage
from CartPage import CartPage
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


def test_result(driver):
    main_shop_page = MainShopPage(driver)
    main_shop_page.autorization()
    main_shop_page.buy_items()
    main_shop_page.checkout_button()
    main_shop_page = CartPage(driver)
    main_shop_page.login()
    main_shop_page = MainShopPage(driver)
    main_shop_page.total()
    
    price = MainShopPage(driver).total()
    assert price == 'Total: $58.29'
