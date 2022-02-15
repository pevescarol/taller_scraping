import requests
from bs4 import BeautifulSoup

pagScrapy = "https://www.investing.com"

head = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}

page = requests.get(pagScrapy, headers=head)

soup = BeautifulSoup(page.text, "html.parser")

print(soup.title.string)