import requests
from bs4 import BeautifulSoup


url = 'https://wallpaperscraft.ru/all/3840x2160/page2'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('a', class_='wallpapers__link')

#print(quotes)

for quote in quotes:
    print(quote.get('href'))
    #print(quote.text)

print("The END!")
