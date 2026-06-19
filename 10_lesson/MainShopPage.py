from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainShopPage:
    def __init__(self, driver):
        """
        Конструктор класса MainShopPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.user_pass = ((By.CSS_SELECTOR, 'input[name="user-name"]'),
                          (By.CSS_SELECTOR, 'input[name="password"]'))
        self.items = ((By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack'), (
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt'), (
                By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie'))
        self.checkout = (By.CSS_SELECTOR, '#checkout')
        self.total_price = ((By.CSS_SELECTOR,
                             'div[class="summary_total_label"]'))

    @allure.step("Авторизация на странице магазина {user_pass}")
    def autorization(self):
        """
        Вводит данные пользователя и нажимает кнопку авторизации

        :param user_pass: str — текста полей куда нужно ввести логин и пароль.
        :param #login_button: str — текст на кнопке, которую нужно нажать.
        """
        self.driver.find_element(*self.user_pass[0]).send_keys('standard_user')
        self.driver.find_element(*self.user_pass[1]).send_keys('secret_sauce')
        self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    @allure.step("Выбор вещей {items} для покупки на странице магазина")
    def buy_items(self):
        """
        Выбирает вещи и нажимает кнопку выбора

        :param items: list[str] — список текстов на кнопках,
        которые нужно нажать.
        """
        self.driver.find_element(*self.items[0]).click()
        self.driver.find_element(*self.items[1]).click()
        self.driver.find_element(*self.items[2]).click()
        self.driver.find_element(
            By.CSS_SELECTOR, 'a[class="shopping_cart_link"]').click()

    @allure.step("Проверка наличия вещей на странице магазина"
                 " путем нажатия кнопки-проверки {checkout}")
    def checkout_button(self):
        """
        Проверяет наличие вещей в корзине

        :param checkout: str — текст на кнопке, которую нужно нажать.
        """
        self.driver.find_element(*self.checkout).click()

    @allure.step("Проверка итоговой суммы "
                 "{total_price} вещей на странице магазина")
    def total(self):
        """
        Проверяет итоговую сумму c задержкой в 30 сек

        :param total_price: str — итоговая сумма корзины.
        """
        total_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(self.total_price)
            )
        return total_element.text
