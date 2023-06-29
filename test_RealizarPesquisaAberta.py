import time
import pytest
from selenium.webdriver.common.by import By
import conftest


@pytest.mark.usefixtures("setup_teardown")
class TestBusca:
        def test_Teste1(self):
            browser = conftest.browser
            lupa = browser.find_element(By.ID, "menuSearch")
            #click()
            lupa.click()
            assert lupa.is_displayed()


        def test_Teste2(self):
            browser = conftest.browser
            lupa = browser.find_element(By.ID, "menuSearch")
            #click()
            lupa.click()
            assert lupa.is_displayed()
