import requests
from bs4 import BeautifulSoup


pages = 3
site = "https://wallpaperscraft.ru/"
url = site + "all/page"
links = []
linksImage = []

for i in range(pages):
    response = requests.get(url+str(i))
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('a', class_='wallpapers__link')

    for quote in quotes:
        links.append(quote.get('href'))
        #print(quote.text)

for link in links:
    response = requests.get(site + link)
    soup = BeautifulSoup(response.text, 'lxml')
    linksImg = soup.find_all('img', class_='wallpaper__image')

    for linkImg in linksImg:
        linksImage.append(linkImg.get('src'))


print("======")
print("Со страниц " + str(len(links)) + " ссылок!")
print("Ссылок на картинки: " + str(len(linksImage)) + " шт.\n")
#print(links)
#print(linksImage)
print("======")
