import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/PS5-Playstation-Wireless-Controller-External/dp/B099K1TQ3Z/ref=sr_1_2?dchild=1&keywords=playstation%2B5&qid=1627589682&sr=8-2&th=1'

#headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36,'}
headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64)', 'Cache-Control': 'no-cache', "Pragma": "no-cache"}
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')


title = soup.find( id = "productTitle").get_text()
price = soup.find( id = "priceblock_ourprice").get_text()
converted_price_string = price[1:6]
converted_price = float(converted_price_string.replace(',',''))


print(converted_price)
print(title.strip(), price.strip())
#print (soup)