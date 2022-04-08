import requests
from bs4 import BeautifulSoup


pages = 2
url = "https://wallpaperscraft.ru/all/3840x2160/page"
links = []

for i in range(pages):
    response = requests.get(url+str(i))
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('a', class_='wallpapers__link')

    for quote in quotes:
        links.append(quote.get('href'))
        #print(quote.text)

print("======\nВ массиве " + str(len(links)) + " ссылок!")
print(links)
print("======")
