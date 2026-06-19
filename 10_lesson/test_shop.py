from selenium import webdriver
from MainShopPage import MainShopPage
from CartPage import CartPage
import pytest
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации открытия страницы и завершения работы драйвера.
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


@allure.title("Тестирование страницы магазина")
@allure.description("Тест проверяет корректность работы страницы магазина"
                    " путем выполнения различных операций.")
@allure.feature("Страница магазина")
@allure.severity(allure.severity_level.CRITICAL)
def test_result(driver):
    """
    Тест проверяет работу страницы магазина
      путем выполнения различных операций.

    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    :param autorization: str — авторизация на сайте.
    :param buy_items: str — покупка вещей на сайте.
    :param checkout_button: str — кнопка проверки корзины.
    :param login: str — заполнение данных пользователя.
    :param total: str — Итоговая цена покупки .
    """
    main_shop_page = MainShopPage(driver)
    with allure.step("Авторизация на странице магазина"):
        main_shop_page.autorization()
    with allure.step("Выбор вещей на странице магазина"):
        main_shop_page.buy_items()
    with allure.step("Проверка корзины на наличие выбранных вещей"):
        main_shop_page.checkout_button()
        main_shop_page = CartPage(driver)
    with allure.step("Заполнение данных пользователя"):
        main_shop_page.login()
        main_shop_page = MainShopPage(driver)
    with allure.step("Проверка итоговой суммы"):
        main_shop_page.total()
        price = MainShopPage(driver).total()
        assert price == 'Total: $58.29'
