import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import conftest



class LupaPage:

    def __int__(self):
        self.browser = conftest.browser

    def acessar_lupa(self):
        wait = WebDriverWait(conftest.browser, 10)
        lupa = wait.until(EC.element_to_be_clickable((By.ID, "menuSearch")))
        #lupa = conftest.browser.find_element(By.ID, "menuSearch")
        #teste
        lupa.click()
        close = conftest.browser.find_element(By.CSS_SELECTOR, "#search > div > div > img")
        assert close.is_enabled()
