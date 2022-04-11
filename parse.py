import requests
from bs4 import BeautifulSoup
import sqlite3


pages = 3
site = "https://wallpaperscraft.ru/"
url = site + "catalog/city/page"
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

#print(linksImage)


print("======")
print("Со страниц " + str(len(links)) + " ссылок!")
print("Ссылок на картинки: " + str(len(linksImage)) + " шт.\n")
#print(links)
#print(linksImage)
print("======")

go = input("Добавляем в базу данных? (y/n)\n")
if go == "y":
    print("Добавляем...")
    try:
        for i in linksImage:
            sqlite_connection = sqlite3.connect('app/app/db.sqlite3')
            cursor = sqlite_connection.cursor()
            sqlite_select_query = "INSERT INTO main_images (link, desk, category) VALUES ('" + i + "','deskription','city');"
            cursor.execute(sqlite_select_query)
            sqlite_connection.commit()
            cursor.close()
            print(i)
    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
