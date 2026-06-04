from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.first_name = (By.CSS_SELECTOR, '#first-name')
        self.last_name = (By.CSS_SELECTOR, '#last-name')
        self.postal = (By.CSS_SELECTOR, '#postal-code')

    def login(self):
        self.driver.find_element(*self.first_name).send_keys('Dmitry')
        self.driver.find_element(*self.last_name).send_keys('Larionov')
        self.driver.find_element(*self.postal).send_keys('424000')
        self.driver.find_element(By.CSS_SELECTOR, '#continue').click()