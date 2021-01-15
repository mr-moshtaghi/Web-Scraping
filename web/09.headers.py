import requests

url = 'http://www.webscrapingfordatascience.com/usercheck/'

myHeader = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}

r = requests.get(url , headers=myHeader)

print(r.text)

print('----------------------------------------------------------------------')

url = ' http://www.webscrapingfordatascience.com/referercheck/secret.php'

myHeader = {
    # 'Referer':'http://www.webscrapingfordatascience.com/referercheck/'
}

r = requests.get(url , headers=myHeader)

print(r.text)