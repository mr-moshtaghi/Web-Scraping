import requests

url = 'http://www.webscrapingfordatascience.com/basichttp/'

result = requests.get(url)

print(result.text)