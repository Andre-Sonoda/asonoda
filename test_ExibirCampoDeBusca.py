import time
import pytest
from selenium.webdriver.common.by import By
import conftest

@pytest.mark.usefixtures("setup_teardown")
class TestBusca:
    def test_ExibirCampoBusca(self):
        browser = conftest.browser
        #find elemente()
        lupa = browser.find_element(By.ID, "menuSearch")

        #clickc()
        lupa.click()
        assert lupa.is_displayed()
        time.sleep(5)
