import time
from threading import Event
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import conftest
from pages.lupa import LupaPage


@pytest.mark.usefixtures("setup_teardown")
class TestBusca:
    def test_RealizarPesquisaAberta(self):
        browser = conftest.browser
        novaLupa = LupaPage()
        novaLupa.acessar_lupa()
        delay = 5
        Event().wait(delay)
        novaLupa = LupaPage()
        novaLupa.acessar_lupa()
        Texto = conftest.browser.find_element(By.ID, "searchResultLabel")
        assert Texto.is_enabled()
