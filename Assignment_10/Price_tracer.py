import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.in/Gvnd-Earrings-Sculpture-Decoration-Sculptures/dp/B0CP9LH7GV/"

user = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0"
}

response = requests.get(URL, headers=user)

soup = BeautifulSoup(response.text, "html.parser")

price = soup.find("span", class_="a-price-whole")

if price:
    price_text = price.get_text()
    print("Price:", price_text)

    price_number = int(price_text.replace(".", "").replace(",", ""))

    target_price = 50000

    if price_number <= target_price:
        print("Buy now! Price is below target.")
    else:
        print("Price is still high.")
else:
    print("Could not find the price.")