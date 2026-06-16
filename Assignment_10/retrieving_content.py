import requests

url = "https://www.amazon.in/"
response = requests.get(url)

print(response)
print(response.status_code)
print(response.text)