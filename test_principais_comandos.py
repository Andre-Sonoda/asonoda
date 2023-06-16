import time
from selenium import webdriver

browser = webdriver.Chrome()

#maximizar browser
browser.maximize_window()

browser.get('https://google.com')
time.sleep(10)

#refresh browser
browser.refresh()

browser.get('https://advantageonlineshopping.com')
time.sleep(10)

#back browser
browser.back()
time.sleep(10)

browser.forward()
time.sleep(10)

#browser.switch_to.new_window("tab")
#time.sleep(10)
#
#close browser
#browser.close()
#time.sleep(10)

#quit
browser.switch_to.new_window("tab")
browser.switch_to.new_window("tab")
time.sleep(10)
browser.quit()
