from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


def test_fill_form():
    driver = webdriver.Edge()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")

    driver.find_element(By.NAME, "zip-code").send_keys("")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")


    driver.find_element(By.XPATH, "//button[text()='Submit']").click()

    WebDriverWait(driver, 25).until(EC.visibility_of_element_located((By.ID, 'zip-code')))


    zip_code_field = driver.find_element(By.ID, 'zip-code')
    background_color = zip_code_field.value_of_css_property('background-color')
    assert background_color == 'rgba(248, 215, 218, 1)' 

    fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]

    for field in fields:
        element = driver.find_element(By.ID, field)
    background_color = element.value_of_css_property('background-color')
    assert background_color == 'rgba(209, 231, 221, 1)'

    driver.quit()