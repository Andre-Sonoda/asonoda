import time

from selenium.webdriver.common.by import By
import conftest
from selenium import webdriver

class LupaPage:

    def __int__(self):
        self.browser = conftest.browser

    def acessar_lupa(self):
        lupa = conftest.browser.find_element(By.ID, "menuSearch")
        lupa.click()
        assert lupa.is_displayed()
