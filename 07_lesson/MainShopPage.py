from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainShopPage:

    def __init__(self, driver):
        self.driver = driver
        self.user_pass = ((By.CSS_SELECTOR, '#user-name'),
                          (By.CSS_SELECTOR, '#password'))
        self.items = ((By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack'), (
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt'), (
                By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie'))
        self.checkout = (By.CSS_SELECTOR, '#checkout')
        self.total_price = (
            By.CSS_SELECTOR, 'div[class="summary_total_label"]')

    def autorization(self):
        self.driver.find_element(*self.user_pass[0]).send_keys('standard_user')
        self.driver.find_element(*self.user_pass[1]).send_keys('secret_sauce')
        self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    def buy_items(self):
        self.driver.find_element([1]).click()
        self.driver.find_element([2]).click()
        self.driver.find_element([3]).click()
        self.driver.find_element(
            By.CSS_SELECTOR, 'a[class="shopping_cart_link"]').click()

    def checkout_button(self):
        self.driver.find_element(*self.checkout).click()

    def total(self):
        total = WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(*self.total_price, "$58.29"))
        total()
