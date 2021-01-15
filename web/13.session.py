import requests

url = 'http://www.webscrapingfordatascience.com/trickylogin/'

MySession = requests.Session()

# MySession.headers.update({'User-Agent':'sajjad'})

r = MySession.get(url)

dataPost = {
    'username':'sajjad',
    'password':'sajjad'
}

r = MySession.post(
    url,
    data=dataPost,
    params={'p':'login'},
    
)

r = MySession.get(url , params={'p':'protected'})

print(r.text)