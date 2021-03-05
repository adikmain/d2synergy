import requests
from bs4 import BeautifulSoup
import sqlite3 as sql

# 1. URL - parsing new data from dotabuff.com
# 2. HEADERS - don't let them think that you're robot
# 3. heroes - list, we gon append here some information via our parser
URL = 'https://www.dotabuff.com/heroes/damage'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/88.0.4324.150 Safari/537.36',
    'accept': '*/*'}
heroes = []


def get_heroes():
    return heroes


# Cookin' some html page
def get_html(url, params=None):
    return requests.get(url, headers=HEADERS, params=params)


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('tr')

    for item in items:
        try:
            heroes.append(item.find_all('td'))
        except AttributeError:
            continue

    del heroes[0]


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

with sql.connect('../dbuff.db') as con:
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
        ready = heroes[i][1].text, heroes[i][2].text, heroes[i][3].text, heroes[i][4].text
        # Created tuple to make import easier
        con.execute('insert into Heroes values (?,?,?,?)', ready)

        # Commit and stay good
    con.commit()
