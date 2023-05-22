import requests

url = 'http://www.webscrapingfordatascience.com/trickylogin/'

MySession = requests.Session()

MySession.headers.update({'User-Agent': 'sajjad'})

r = MySession.get(url)

print(r)

dataPost = {
    'username': 'sajjad',
    'password': 'sajjad'
}

r = MySession.post(
    url,
    data=dataPost,
    params={'p': 'login'},

)

print(r)

r = MySession.get(url, params={'p': 'protected'})

print(r.request.headers)
print(r.text)
