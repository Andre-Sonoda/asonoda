import pytest
from selenium import webdriver

browser: webdriver.Remote

@pytest.fixture
def setup_teardown():
    #setup
    global browser
    browser = webdriver.Chrome()
    browser.implicitly_wait(20)
    browser.maximize_window()
    browser.get("https://advantageonlineshopping.com/")

    # run test
    yield

    # teardown
    browser.quit()
