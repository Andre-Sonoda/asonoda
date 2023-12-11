import conftest

class BasePage:
    def __int__(self):
        self.browser = conftest.browser

    def encontrar_elemento(self, locator):
        return self.browser.find_element(*locator)

    def encontrar_elementos(self, locator):
        return self.browser.find_elements(*locator)
