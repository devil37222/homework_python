from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/login")

driver.find_element(By.ID, 'username').send_keys("tomsmith")

driver.find_element(By.ID, 'password').send_keys("SuperSecretPassword!")

driver.find_element(By.CSS_SELECTOR, 'i').click()

message = driver.find_element(By.XPATH, 'div#flash.flash.success')
print(message.text)

driver.quit()