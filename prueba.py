import requests
from bs4 import BeautifulSoup

pagScrapy = "https://www.investing.com"

head = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}

page = requests.get(pagScrapy, headers=head)

soup = BeautifulSoup(page.text, "html.parser")

# print(soup.title.string)

table_crypto = soup.find(class_='genTbl js-all-crypto-preview-table wideTbl elpTbl elp20 topCryptoHP')
tr_all = table_crypto.find_all('tr', {'i': '1057391'})

price = tr_all[0].find_all('td', {'class': 'price js-currency-price'})

print(f"Valor del Bitcoin (USD): {price[0].get_text()}")
