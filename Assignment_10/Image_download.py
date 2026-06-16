import requests

url = "https://static.vecteezy.com/system/resources/previews/024/804/557/original/pikachu-art-or-illustration-on-pickachu-free-vector.jpg"
user = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"
}

response = requests.get(url = url, headers = user)
pic = response.content

f = open('pikachu-art-or-illustration-on-pickachu-free-vector.jpg', 'wb')
f.write(pic)