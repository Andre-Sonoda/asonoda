import time
import pytest
from selenium.webdriver.common.by import By
import conftest


@pytest.mark.usefixtures("setup_teardown")
class TestBusca:
        def test_Teste1(self):
            browser = conftest.browser
            lupa = browser.find_element(By.ID, "menuSearch")
            # click()
            lupa.click()


        def test_Teste2(self):
            browser = conftest.browser
            busca = browser.find_element(By.ID, "autoComplete")
            # send_keys()
            busca.send_keys("Teste")


        def test_Teste3(self):
            browser = conftest.browser
            lupa = browser.find_element(By.ID, "menuSearch")
            # click()
            lupa.click()

            text_esperado = 'No results for "Teste"'
            text_obtido = 'No results for "Teste"'
            assert text_esperado in text_obtido, f"Esperado {text_esperado}. Atual {text_obtido}."
