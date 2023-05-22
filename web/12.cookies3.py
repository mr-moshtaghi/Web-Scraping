import requests

url = 'http://www.webscrapingfordatascience.com/trickylogin/'

request_get_1 = requests.get(url)

get_cookie = {
    'PHPSESSID': request_get_1.cookies['PHPSESSID']
}

dataPost = {
    'username': 'sajjad',
    'password': 'sajjad'
}

request_post = requests.post(
    url,
    data=dataPost,
    cookies=get_cookie,
    params={'p': 'login'},
    allow_redirects=False
)

post_cookie = {
    'PHPSESSID': request_post.cookies['PHPSESSID']
}

request_get_2 = requests.get(url, params={'p': 'protected'}, cookies=post_cookie)

print(request_get_2.text)
