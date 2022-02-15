import requests

pagScrapy = "https://www.investing.com"

page = requests.get(pagScrapy)

print(page)
