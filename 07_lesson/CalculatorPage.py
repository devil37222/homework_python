from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay = ((By.CSS_SELECTOR, "#delay"))
        self.button = ((By.XPATH, '//span[text()="7"]'), (By.XPATH, '//span[text()="+"]'), (By.XPATH, '//span[text()="8"]'), (By.XPATH, '//span[text()="="]'))
        self.results_selector = (By.CSS_SELECTOR, 'div[class="screen"]')

    def delay(self): 
        self.delay.clear()
        self.driver.find_element(*self.delay).send_keys("45")

    def button(self):
        self.button = self.driver.find_element('*self.button[1]').click()
        self.button = self.driver.find_element('*self.button[2]').click()
        self.button = self.driver.find_element('*self.button[3]').click()
        self.button = self.driver.find_element('*self.button[4]').click()
        
    def get_search_results(self):
        self.get_search_results = WebDriverWait(self.driver, 45).until(EC.text_to_be_present_in_element(*self.results_selector, '15'))
        result = button_page.get_search_results()