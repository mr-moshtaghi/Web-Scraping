import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes'
r = requests.get(url)

content = BeautifulSoup(r.text, 'html.parser')

episodes = []
# EPTable = content.findAll('table' , 'wikiepisodetable')
EPTable = content.select('table.wikiepisodetable')[:8]

for table in EPTable:
    headers = []
    rows = table.findAll('tr')
    for header in table.find('tr').findAll('th'):
        headers.append(header.text)
    for row in table.findAll('tr')[1:]:
        values = []
        for col in row.findAll(['th', 'td']):
            values.append(col.text)
        if values:
            episodeDict = {headers[i]: values[i] for i in range(len(values))}
            episodes.append(episodeDict)

for ep in episodes:
    print(ep)
