import requests
from bs4 import BeautifulSoup
import re

url = 'https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes'

contents = BeautifulSoup(requests.get(url).text , 'html.parser')

result1 = contents.find(re.compile('^d')) 

result2 = contents.select('a')

result3 = contents.select('a' , limit=5)

result4 = contents.select('#p-logo')

result5 = contents.select('div#p-logo') # ======>tag div with id:p-logo

result6 = contents.select('tr.vevent') # =======>tag tr with class:vevent

result7 = contents.select('a[href^="/wiki/"]')

result8 = contents.select('ul > li')  

