from selenium import webdriver

url = 'http://www.webscrapingfordatascience.com/complexjavascript/'

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(url)

for q in driver.find_elements_by_class_name('quote'):
    print(q.text)

input('Enter to Exit ...')

driver.quit()
