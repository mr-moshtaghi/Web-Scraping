from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("/home/sajjad/Documents/Web-Scraping/web/chromedriver")
driver.get('http://www.webscrapingfordatascience.com/complexjavascript/')

quoteElements = WebDriverWait(driver , 5).until(
    EC.presence_of_all_elements_located(
        # (By.CLASS_NAME, 'quate')
        (By.CSS_SELECTOR, '.quote')
    )
)

for q in quoteElements:
    print(q.text)