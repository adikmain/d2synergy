import requests
from bs4 import BeautifulSoup
import sqlite3 as sq

# 1. URL - ссылка на то, что будем парсить
# 2. HEADERS - хз, чтобы не подумали что бот
# 3. heroes - то с чем будем работать
URL = 'https://www.dotabuff.com/heroes/damage'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'accept': '*/*'}
heroes = []


# Эта функция вроде как просто даёт нам фулл копию страницы в виде HTMl
def get_html(url, params=None):
    return requests.get(url, headers=HEADERS, params=params)


# Не люблю функции, но тут она че то делает (подключение к библиотекам тырыпыры)
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    # 2 аргумента у супа, перый это уже готовый html текст взятый из requests(выше функция)
    #   + нужно указать ЧЕГО это парсер
    items = soup.find_all('tr')  # Поиск по всем <tr>

    # Нам суп выдал (по сути нашёл все <tr> содержащие элементы в том документе повыше) Пытается прочекировать все
    # значения, с помощью параметра separator можно их разделить пробелом(но с героями например Keeper of The light
    # это плохо работает)

    for item in items:
        try:
            heroes.append(item.get_text(separator=' '))
        except AttributeError:
            continue

    # Эта хуйня вызывала ошибку AttributeError, потому что первым ITEM из ITEMS на дбаффе почему то пустые слоты
    del heroes[0]
    for k in range(len(heroes)):
        heroes[k] = heroes[k].split(' ')
    # Сам сепарировал, теперь засплитил, чтобы четко в одном листе было разделение кто че кто где

    #  Правильное разделение после парсера, решает проблему с котлом и квопой
    for j in range(len(heroes)):
        if len(heroes[j]) == 6:
            heroes[j][0] = heroes[j][0] + ' ' + heroes[j][1] + ' ' + heroes[j][2]
            for _ in range(2):
                del heroes[j][1]

        elif len(heroes[j]) == 7:
            heroes[j][0] = heroes[j][0] + ' ' + heroes[j][1] + ' ' + heroes[j][2] + ' ' + heroes[j][3]
            for _ in range(3):
                del heroes[j][1]

        elif len(heroes[j]) > 4:
            heroes[j][0] = heroes[j][0] + ' ' + heroes[j][1]
            del heroes[j][1]


# я не знаю че это)0
def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error, not 200')


# Вызывал функцию получается
parse()

# Подключаюсь к БД
with sq.connect('adilek.db') as con:
    cur = con.cursor()
    cur.execute('''DROP TABLE IF EXISTS Heroes''')  # Каждый раз когда я запускаю маин.пу, таблица будет удаляться
    cur.execute('''
            CREATE TABLE IF NOT EXISTS Heroes(
            name text,
            damage text,
            tower text,
            heal text
            ) 
            ''')  # Но потом опять создаваться, чтобы иметь свежие данные
    # Цикл, чтобы закинуть все данные в БД
    for i in range(len(heroes)):
        ready = heroes[i][0], heroes[i][-3], heroes[i][-2], heroes[i][-1]
        # Создал специальный тупл, чтобы удобно запихать в бд
        con.execute('insert into Heroes values (?,?,?,?)', ready)  # Столько ёбки было с этим пунктом, приходило 8 value
        # Но бд могла записывать только 4 из них, пришлось стучаться до 1 и 3 последних элементов листа,
        # Все из за Queen of Pain и Keeper of The Light

        # Закоммитил, остался рад
    con.commit()

