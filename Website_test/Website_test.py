import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://example.com")
title = driver.title
subject = "Example"
orig_site = "https://www.iana.org/help/example-domains"
el = "body > div > p:nth-child(3) > a"

if subject in title:
    driver.find_element(By.CSS_SELECTOR, el).click()
    print("Вы перешли на правильный сайт.") if driver.current_url == orig_site else print("Кажется, сайт обновили, это не он.")
else:
    print("Неверный сайт, заголовок не совпал!")

time.sleep(5)
driver.quit()
print("Программа завершена!")
