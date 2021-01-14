import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes'
result = requests.get(url)

contents = BeautifulSoup(result.text , 'html.parser')

print(contents.find('' , attrs = {'id':'p-logo' , 'role':'banner'}))
print('----------------------------------------------------')

print(contents.find('' , class_='vevent'))
print('----------------------------------------------------')

print(len(contents.findAll('' , class_='vevent' , limit=10)))
print(len(contents.findAll('' , class_='vevent' )))

