import time
import pytest
from selenium.webdriver.common.by import By
import conftest


@pytest.mark.usefixtures("setup_teardown")
class TestBusca:
        def test_Teste1(self):
            browser = conftest.browser
            # find element()
            lupa = browser.find_element(By.ID, "menuSearch")
            # click()
            lupa.click()
            time.sleep(5)

           # find element()
            close = browser.find_element(By.CSS_SELECTOR, "#search > div > div > img")
            # click()
            close.click()
            assert close.is_displayed()

