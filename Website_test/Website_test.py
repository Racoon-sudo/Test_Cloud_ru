from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get("https://example.com")
title = driver.title
sub = "Example"
orig_site = "https://www.iana.org/help/example-domains"

if sub in title:
    driver.find_elements(By.CSS_SELECTOR, "#body > div:nth-child(1) > p:nth-child(3) > a:nth-child(1)")
    driver.find_element(By.LINK_TEXT, "More information...").click()
    if driver.current_url == orig_site:
        print("Вы перешли на правильный сайт!")
    else:
        print("Кажется, сайт обновили, это не он.")
else:
    print("Неверный сайт, заголовок не совпал!")

time.sleep(5)
driver.quit()
print("Программа завершена!")