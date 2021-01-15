import requests

url = 'http://www.webscrapingfordatascience.com/postform2/'

formsData = {
    'name':'sajad',
    'gender':'M',
    'pazza':'like',
    'commends':'i am sajad'
}

result = requests.post(url , data=formsData)

print(result.text)