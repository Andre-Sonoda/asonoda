from selenium import webdriver
from selenium.webdriver.common.by import By

browser: webdriver = webdriver.Chrome()
browser.implicitly_wait(20)

browser.maximize_window()
browser.get("https://advantageonlineshopping.com/")

# find element()
def test_Teste1():
    lupa = browser.find_element(By.ID, "menuSearch")
# click()
    lupa.click()

def test_Teste2():
    busca = browser.find_element(By.NAME, "mobile_search")
# send_keys()
    busca.send_keys("Teste")
