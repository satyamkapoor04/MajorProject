import requests
from bs4 import BeautifulSoup as bs

a = input("Enter a word to find synonyms for from thesaurus.com\n")
url = 'https://www.thesaurus.com/browse/' + str(a)
page = requests.get(url)

soup = bs(page.text, 'html.parser')

find = soup.find_all(class_='css-1gk8jl3 etbu2a31')

for i in find:
    print(i.get_text())

