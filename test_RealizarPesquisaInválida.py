import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://advantageonlineshopping.com/")
time.sleep(10)

# find element()
lupa = browser.find_element(By.ID, "menuSearch")
time.sleep(10)

# click()
lupa.click()
time.sleep(10)
assert lupa.is_displayed()

# find element()
browser.find_element(By.NAME, "mobile_search").send_keys("Teste")
time.sleep(5)

# click()
lupa.click()
time.sleep(10)
assert lupa.is_displayed()
