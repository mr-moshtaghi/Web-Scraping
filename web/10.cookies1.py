import requests 

url = 'http://www.webscrapingfordatascience.com/cookielogin/'

dataPost = {
    'username':'sajjad',
    'password':'sajjad',   
}

request_post = requests.post(url , data=dataPost)

myCookies ={
    'PHPSESSID':request_post.cookies['PHPSESSID']
} 



request_get = requests.get(url + 'secret.php' , cookies=myCookies)

print(request_get.text)