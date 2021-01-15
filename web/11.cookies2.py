import requests

url = 'http://www.webscrapingfordatascience.com/redirlogin/'

request_post = requests.post(url, allow_redirects=False)

print(request_post.cookies)