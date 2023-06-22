import time

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
    busca = browser.find_element(By.ID, "autoComplete")
    # send_keys()
    busca.send_keys("Teste")


def test_Teste3():
    lupa = browser.find_element(By.ID, "menuSearch")
    # click()
    lupa.click()

    text_esperado = 'No results for "Teste"'
    text_obtido = 'No results for "Teste"'
    assert text_esperado in text_obtido, f"Esperado {text_esperado}. Atual {text_obtido}."
