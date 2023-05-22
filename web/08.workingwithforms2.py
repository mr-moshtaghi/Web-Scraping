import requests
from bs4 import BeautifulSoup

url = 'http://www.webscrapingfordatascience.com/postform3/'

r = requests.get(url)
html = BeautifulSoup(r.text, 'html.parser')
protection = html.find('input', {'name': 'protection'}).get('value')


formsData = {
    'name': 'sajad',
    'gender': 'F',
    'pizza': 'like',
    'commends': 'i am sajad',
    'protection': protection
}

result = requests.post(url, data=formsData)

print(result.text)
