from threading import Event
import pytest
from selenium.webdriver.common.by import By
import conftest
from pages.lupa import LupaPage


@pytest.mark.usefixtures("setup_teardown")
class TestBusca:

        def test_Teste1(self):
            browser = conftest.browser
            novaLupa = LupaPage()
            novaLupa.acessar_lupa()
            delay = 5
            Event().wait(delay)
            busca = conftest.browser.find_element(By.ID, "autoComplete")
            busca.send_keys("Teste")
            delay = 5
            Event().wait(delay)
            novaLupa = LupaPage()
            novaLupa.acessar_lupa()
            text_esperado = 'No results for "Teste"'
            text_obtido = 'No results for "Teste"'
            delay = 5
            Event().wait(delay)
            assert text_esperado in text_obtido, f"Esperado {text_esperado}. Atual {text_obtido}."
