from selenium.webdriver.common.by import By
import allure


class CartPage:
    def __init__(self, driver):
        """
        Конструктор класса CartPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.first_name = (By.CSS_SELECTOR, '#first-name')
        self.last_name = (By.CSS_SELECTOR, '#last-name')
        self.postal = (By.CSS_SELECTOR, '#postal-code')

    @allure.step("Заполнение данных пользователя {"
                 "first_name}:{last_name}:{postal}")
    def login(self):
        """
        Заполнение данных пользователя (имени, фамилии, индекса)
        и нажатие кнопки 'continue'

        :param first_name: str — текст поля имени.
        :param last_name: str — текст поля фамилии.
        :param postal: str — текст поля индекса.
        :param #continue: str — текст на кнопке,на которую нужно нажать.
        """
        self.driver.find_element(*self.first_name).send_keys('Dmitry')
        self.driver.find_element(*self.last_name).send_keys('Larionov')
        self.driver.find_element(*self.postal).send_keys('424000')
        self.driver.find_element(By.CSS_SELECTOR, '#continue').click()
