import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all('script')
print(links)

pic = soup.find_all('img')
print(pic)

