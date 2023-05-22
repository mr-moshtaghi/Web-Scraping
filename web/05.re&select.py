import requests
from bs4 import BeautifulSoup
import re

url = 'https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes'

contents = BeautifulSoup(requests.get(url).text, 'html.parser')

result1 = contents.find(re.compile('^d'))

print(result1)
print("---------------------------------------------------------------")

# result2 = contents.select('a')
#
# print(result2)
# print("---------------------------------------------------------------")
#
# result3 = contents.select('a', limit=5)
#
# print(result3)
# print("---------------------------------------------------------------")
#
# result4 = contents.select('#p-logo')
#
# print(result4)
# print("---------------------------------------------------------------")
#
# result5 = contents.select('div#p-logo')  # ======>tag div with id:p-logo
#
# print(result5)
# print("---------------------------------------------------------------")
#
# result6 = contents.select('tr.vevent')  # =======>tag tr with class:vevent
#
# print(result6)
# print("---------------------------------------------------------------")
#
# result7 = contents.select('a[href^="/wiki/"]')
#
# print(result7)
# print("---------------------------------------------------------------")
#
# result8 = contents.select('ul > li')
#
# print(result8)
# print("---------------------------------------------------------------")
