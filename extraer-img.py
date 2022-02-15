import requests
from bs4 import BeautifulSoup

url = "https://www.wingedstore.com/framesets-55"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
print(soup.title.string)

images = []
img = soup.find("ul", {"class": "clear thumbnails grid row lista_prodotti"}).findAll("img")
for item in img:
    images.append(item["src"])


# Descargamos la imagen
i = 0
for url in images:
    photo = requests.get(url).content
    with open(str(i)+".jpg", "wb")as handle:
        handle.write(photo)
    i += 1
