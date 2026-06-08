from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class MainShopPage:

    def __init__(self, driver):
        self.driver = driver
        self.user_pass = ((By.CSS_SELECTOR, 'input[name="user-name"]'),
                          (By.CSS_SELECTOR, 'input[name="password"]'))
        self.items = ((By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack'), (
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt'), (
                By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie'))
        self.checkout = (By.CSS_SELECTOR, '#checkout')
        self.total_price = ((By.CSS_SELECTOR,
                             'div[class="summary_total_label"]'))

    def autorization(self):
        self.driver.find_element(*self.user_pass[0]).send_keys('standard_user')
        self.driver.find_element(*self.user_pass[1]).send_keys('secret_sauce')
        self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    def buy_items(self):
        self.driver.find_element(*self.items[0]).click()
        self.driver.find_element(*self.items[1]).click()
        self.driver.find_element(*self.items[2]).click()
        self.driver.find_element(
            By.CSS_SELECTOR, 'a[class="shopping_cart_link"]').click()

    def checkout_button(self):
        self.driver.find_element(*self.checkout).click()

    def total(self):
        total_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(self.total_price)
            )
        return total_element.text
