import requests
from bs4 import BeautifulSoup
import sqlite3 as sql

# 1. URL - parsing new data from dotabuff.com
# 2. HEADERS - don't let them think that you're robot
# 3. heroes - list, we gon append here some information via our parser
URL = 'https://www.dotabuff.com/heroes/damage'
TIME_URL = 'https://www.dotabuff.com/heroes/impact'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/88.0.4324.150 Safari/537.36',
    'accept': '*/*'}
heroes = []
timers = []

heroes_complete = []
timers_complete = []


def get_heroes():
    return heroes_complete


def get_tempo():
    return timers_complete


# Cookin' some html page
def get_html(url, params=None):
    return requests.get(url, headers=HEADERS, params=params)


def get_content(html, array):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('tr')

    for item in items:
        try:
            array.append(item.find_all('td'))

        except AttributeError:
            continue

    del array[0]


# Main parse function
def parse(address, array):
    html = get_html(address)
    if html.status_code == 200:
        get_content(html.text, array)
    else:
        print('Error, not 200')


parse(URL, heroes)
parse(TIME_URL, timers)

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
        heroes_complete.append([x for x in ready])
        # Commit and stay good
    con.commit()

    cur.execute('''DROP TABLE IF EXISTS Timers''')
    cur.execute('''
                CREATE TABLE IF NOT EXISTS Timers(
                name text,
                timer text
                ) 
                ''')
    for j in range(len(heroes)):
        ready = timers[j][1].text, timers[j][-1].text
        # Created tuple to make import easier
        con.execute('insert into Timers values (?,?)', ready)
        timers_complete.append([x for x in ready])
        # Commit and stay good
    con.commit()
