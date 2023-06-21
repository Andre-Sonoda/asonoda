from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import browser

def test_Teste1():
    browser: webdriver = webdriver.Chrome()
    browser.implicitly_wait(20)

    browser.maximize_window()
    browser.get("https://advantageonlineshopping.com/")

# find element()
def test_Teste2():
    lupa = browser.find_element(By.ID, "menuSearch")
    campo_busca = browser.find_element(By.NAME, "mobile_search")

#click()
    lupa.click()

#send_keys()
    campo_busca.send_keys("Teste")
