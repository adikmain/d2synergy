from hero_stats import durable_tier, damage_tier, disable_tier, tower_tier, heal_tier, save_tier, \
    escape_tier, heroes_list, tempo_tier, anti_heal_list
import sqlite3 as sql


class Hero:
    RANGES = [0.1, 0.3, 0.5, 0.7, 0.9]

    def __init__(self, name):
        self.damage = 0
        self.heal = 0
        self.tower = 0
        self.disable = 0
        self.save = 0
        self.escape = 0
        self.durable = 0
        self.anti_heal = 0
        self.tempo = 0
        self.name = name
        self.init_stats()

    def __str__(self):
        return f'Hero: {self.name}\n' \
               f'Damage: {self.damage}\n' \
               f'Heal potential: {self.heal}\n' \
               f'Push potential: {self.tower}\n' \
               f'Disable potential: {self.disable}\n' \
               f'Save options: {self.save}\n' \
               f'Escape options: {self.escape}\n' \
               f'Hero durability: {self.durable}' \
               f'Anti-heal: {self.anti_heal}' \
               f"Hero's tempo: {self.tempo}"

    def init_stats(self):
        for i in Hero.RANGES:
            if self.name in damage_tier[str(i)]:
                self.damage += i
            if self.name in heal_tier[str(i)]:
                self.heal += i
            if self.name in tower_tier[str(i)]:
                self.tower += i
            if self.name in disable_tier[str(i)]:
                self.disable += i
            if self.name in save_tier[str(i)]:
                self.save += i
            if self.name in escape_tier[str(i)]:
                self.escape += i
            if self.name in durable_tier[str(i)]:
                self.durable += i
            if self.name in tempo_tier[str(i)]:
                self.tempo += i
            if self.name in anti_heal_list[str(i)]:
                self.anti_heal += i
        return self


with sql.connect('../dbuff.db') as con:
    cur = con.cursor()
    cur.execute('''DROP TABLE IF EXISTS Tiers''')
    cur.execute('''create table if not exists Tiers(
            name text primary key ,
            damage integer,
            heal integer,
            tower integer,
            disable integer,
            save integer,
            'escape' integer,
            durable integer,
            tempo integer,
            anti_heal integer

    )''')

    for hero in sorted(heroes_list):
        heroes_parameters = Hero(hero).name, Hero(hero).damage, Hero(hero).heal, Hero(hero).tower, Hero(
            hero).disable, Hero(hero).save, Hero(hero).escape, Hero(hero).durable, Hero(hero).tempo, Hero(
            hero).anti_heal
        cur.execute('insert into Tiers values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', heroes_parameters)
