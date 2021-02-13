from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("/home/sajjad/Documents/Web-Scraping/web/chromedriver")
driver.implicitly_wait(10)
driver.get("http://www.webscrapingfordatascience.com/postform2/")

chain = ActionChains(driver)
chain.send_keys_to_element(driver.find_element_by_name('name'), "Sajjad Moshtaghi")
chain.click(driver.find_element_by_css_selector("input[name='gender'][value='M']"))
chain.click(driver.find_element_by_name("pizza"))
Select(driver.find_element_by_name("haircolor")).select_by_value("blonde")
chain.send_keys_to_element(driver.find_element_by_name("comments"), [
    'how are you?', Keys.ENTER, 'i am a programmer'
])
chain.perform()

input("press enter to submit form ...")
driver.find_element_by_tag_name("form").submit()

input("Enter to exit ...")

driver.quit()
