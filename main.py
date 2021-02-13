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

# Cookin' some html page
def get_html(url, params=None):
    return requests.get(url, headers=HEADERS, params=params)


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('tr')


    for item in items:
        try:
            heroes.append(item.get_text(separator=' '))
        except AttributeError:
            continue

    del heroes[0]
    for k in range(len(heroes)):
        heroes[k] = heroes[k].split(' ')


    # Make taken data sweet
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


# Main parse function
def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error, not 200')


parse()

# Get connected to DB
# Drop and then create table

with sq.connect('adilek.db') as con:
    cur = con.cursor()
    cur.execute('''DROP TABLE IF EXISTS Heroes''')
    cur.execute('''
            CREATE TABLE IF NOT EXISTS Heroes(
            name text,
            damage text,
            tower text,
            heal text
            ) 
            ''')

    for i in range(len(heroes)):
        ready = heroes[i][0], heroes[i][-3], heroes[i][-2], heroes[i][-1]
        # Created tuple to make import easier
        con.execute('insert into Heroes values (?,?,?,?)', ready)

        # Commit and stay good
    con.commit()
