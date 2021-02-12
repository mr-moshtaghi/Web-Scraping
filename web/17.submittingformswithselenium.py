from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/home/sajjad/Documents/Web-Scraping/web/chromedriver")
driver.implicitly_wait(10)
driver.get("http://www.webscrapingfordatascience.com/postform2/")

driver.find_element_by_name('name').send_keys("Sajjad Moshtaghi")
driver.find_element_by_css_selector("input[name='gender'][value='M']")
driver.find_element_by_name("pizza").click()
Select(driver.find_element_by_name("haircolor")).select_by_value("blonde")
driver.find_element_by_name("comments").send_keys(
    ["how are you", Keys.ENTER, "my name is sajjad"]
)

input("press enter to submit form ...")
driver.find_element_by_tag_name("form").submit()

input("Enter to exit ...")

driver.quit()