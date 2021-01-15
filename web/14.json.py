import requests

url = 'http://www.webscrapingfordatascience.com/jsonajax/'

r = requests.post(url + 'results.php', data={'api_code':'C123456'})

print(r.json())
print(r.json().get('results'))
