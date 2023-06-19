import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://advantageonlineshopping.com/")

#find elemente()
lupa = browser.find_element(By.ID, "menuSearch")
time.sleep(10)

#clickc()
lupa.click()
time.sleep(10)
assert lupa.is_displayed()

#find elemente()
lupa = browser.find_element(By.ID, "menuSearch")
time.sleep(10)

#clickc()
lupa.click()
time.sleep(10)
assert lupa.is_displayed()