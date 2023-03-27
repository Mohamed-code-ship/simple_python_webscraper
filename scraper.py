import requests

from bs4 import BeautifulSoup

res = requests.get("https://www.codewithtomi.com/")

soup = BeautifulSoup(res.content, 'html.parser')

print(soup)