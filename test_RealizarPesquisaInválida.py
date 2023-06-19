import time

import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://advantageonlineshopping.com/")
time.sleep(10)

# find elemente()
lupa = browser.find_element(By.ID, "menuSearch")
time.sleep(10)

# click()
lupa.click()
time.sleep(10)
assert lupa.is_displayed()

# find elemente()
browser.find_element(By.NAME, "mobile_search")
self.mobile_search = input(f'Teste')
time.sleep(10)

# click()
lupa.click()
time.sleep(10)
assert lupa.is_displayed()
