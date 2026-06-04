from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_fill_form():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
    driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    driver.find_element(By.CSS_SELECTOR, 'a[class="shopping_cart_link"]').click()

    driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys('Dmitry')
    driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Larionov')
    driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('424000')

    driver.find_element(By.CSS_SELECTOR, '#continue').click()
   
    total = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div[class="summary_total_label"]'), "$58.29"))
    assert total

    driver.quit()
