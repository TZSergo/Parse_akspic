from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import sqlite3, random, os, urllib.request, p


bot = Bot(token=p.token)
dp = Dispatcher(bot)

start_buttons = ['Города', 'Машины', 'Космос', 'Минимализм', 'Арт', 'Вектор', 'Природа']
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(*start_buttons)

masMes = []


def connect_db(category):
    sqlite_connection = sqlite3.connect('../app/app/db.sqlite3')
    cursor = sqlite_connection.cursor()
    sqlite_select_query = f"SELECT link FROM main_images WHERE category = '{category}';"
    cursor.execute(sqlite_select_query)
    sqlite_connection.commit()
    records = cursor.fetchall()
    cursor.close()
    return download_img(records)


def download_img(masImg):
    for row in masImg:
         masMes.append(row[0])
    destination = 'dimg/' + str(random.randint(0, 1000)) + '.jpg'
    urllib.request.urlretrieve(masMes[random.randint(0, len(masImg))], destination)
    masMes.clear()
    return destination


def delete_img(filename):
    os.remove(filename)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Выбери категорию', reply_markup=keyboard)


@dp.message_handler(Text(equals='Города'))
async def city(message: types.Message):
    filename = connect_db('city')
    await message.answer_photo(types.InputFile(filename))
    delete_img(filename)


@dp.message_handler(Text(equals='Жопа'))
async def ass(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer('Это не я жопа, Лера - жопа!', reply_markup=keyboard)


@dp.message_handler(Text(equals='Машины'))
async def cars(message: types.Message):
    filename = connect_db('cars')
    await message.answer_photo(types.InputFile(filename))
    delete_img(filename)


@dp.message_handler(Text(equals='Космос'))
async def cosmos(message: types.Message):
    filename = connect_db('cosmos')
    await message.answer_photo(types.InputFile(filename))
    delete_img(filename)


@dp.message_handler(Text(equals='Минимализм'))
async def minimal(message: types.Message):
    filename = connect_db('minimal')
    await message.answer_photo(types.InputFile(filename))
    delete_img(filename)


@dp.message_handler(Text(equals='Арт'))
async def art(message: types.Message):
    filename = connect_db('art')
    await message.answer_photo(types.InputFile(filename))
    delete_img(filename)


@dp.message_handler(Text(equals='Вектор'))
async def vector(message: types.Message):
    filename = connect_db('vector')
    await message.answer_photo(types.InputFile(filename))
    delete_img(filename)


@dp.message_handler(Text(equals='Природа'))
async def nature(message: types.Message):
    filename = connect_db('nature')
    await message.answer_photo(types.InputFile(filename))
    delete_img(filename)


if __name__ == '__main__':
    executor.start_polling(dp)
