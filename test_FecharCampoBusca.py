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
            close = browser.find_element(By.CSS_SELECTOR, "#search > div > div > img")
            close.click()
            assert close.is_displayed()
