import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes'
result = requests.get(url)

contents = BeautifulSoup(result.text , 'html.parser')

contents.findAll('h2')

for content in contents.findAll('h2'):
    print(content)