import requests

# url = 'http://www.webscrapingfordatascience.com/paramhttp/?query=sajad'

url = 'http://www.webscrapingfordatascience.com/paramhttp/'

parameters = {
    'query':'sajad'
}

result = requests.get(url , params=parameters)

print(result.text)

print('-------------------------------------------------')


url = ' http://www.webscrapingfordatascience.com/calchttp/'

parameters = {
    'a':10,
    'b':5,
    'op':'*'
}

result = requests.get(url , params=parameters)

print(result.text)