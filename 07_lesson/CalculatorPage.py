from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.page = ((By.CSS_SELECTOR, 'input[type="text"]'))
        self.button = ((By.XPATH, '//span[text()="7"]'), (
            By.XPATH, '//span[text()="+"]'), (
                By.XPATH, '//span[text()="8"]'), (
                    By.XPATH, '//span[text()="="]'))
        self.results_selector = ((By.CSS_SELECTOR, 'div[class="screen"]'))

    def delay(self):
        delay_element = self.driver.find_element(*self.page)
        delay_element.clear()
        lesson7
        delay_element.send_keys("45")
        delay_element.send_keys("")

    def button_number(self):
        button_element = self.driver.find_element(*self.button[0]).click()
        button_element = self.driver.find_element(*self.button[1]).click()
        button_element = self.driver.find_element(*self.button[2]).click()
        button_element = self.driver.find_element(*self.button[3]).click()

    def get_search_results(self):
        get_search_results = WebDriverWait(self.driver, 45).until(
            EC.text_to_be_present_in_element(self.results_selector, "15"))
        return get_search_results
