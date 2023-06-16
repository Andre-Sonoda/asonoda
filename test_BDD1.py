from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.maximize_window()
browser.get("https://advantageonlineshopping.com/")

lupa = browser.find_element(By.ID, "menuSearch")
print(lupa.is_displayed())
#assert lupa.is_displayed()
