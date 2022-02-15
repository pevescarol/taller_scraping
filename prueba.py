import requests
from bs4 import BeautifulSoup

pagScrapy = "https://www.investing.com"

head = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}

page = requests.get(pagScrapy, headers=head)

# Extraemos el title
soup = BeautifulSoup(page.text, "html.parser")

print(soup.title.string)

# Extraemos valor de una tabla
table_crypto = soup.find(class_='genTbl js-all-crypto-preview-table wideTbl elpTbl elp20 topCryptoHP')
tr_all = table_crypto.find_all('tr', {'i': '1057391'})
price = tr_all[0].find_all('td', {'class': 'price js-currency-price'})

# print(f"Valor del Bitcoin (USD): {price[0].get_text()}")

# Extraemos mas de un valor de la tabla
tr = table_crypto.find_all('tr')
for sub_tr in tr:
    price2 = sub_tr.find_all('td', {'class': 'price js-currency-price'})
    name = sub_tr.find_all('td', {'class': 'left bold elp name cryptoName first js-currency-name'})
    if name!=[]:
        print(f"Valor en {name[0].get_text()} (USD): {price2[0].get_text()}")