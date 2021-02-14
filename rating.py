from main import heroes as info

# Main lists
heroes_list = []
heal_list = []
tower_list = []
damage_list = []
info = [[y.text for y in x[1:]] for x in info]


def getHeroes(names):
    for i in range(len(info)):
        names.append(info[i][0])


getHeroes(heroes_list)


# Heal tier list

def getHeal(heroes):
    for i in range(len(info)):
        heroes.append([float(info[i][3]), info[i][0]])


getHeal(heal_list)


# Sorting tier list
def sortHeal():
    for v in range(len(heal_list)):
        heal_list[v][0] = (heal_list[v][0] / max(heal_list)[0])


sortHeal()


# Tower damage tier list

def getTower(heroes):
    for i in range(len(info)):
        heroes.append([float(info[i][2]), info[i][0]])
    for v in range(len(heroes)):
        heroes[v][0] = (heroes[v][0] / max(heroes)[0])


getTower(tower_list)


# Hero damage tier list
def getDamage(heroes):
    for i in range(len(info)):
        if ',' in info[i][1]:
            info[i][1] = info[i][1].replace(',', '')
        heroes.append([float(info[i][1]), info[i][0]])
    top_damage = max(heroes)[0]
    for v in range(len(heroes)):
        heroes[v][0] /= top_damage


getDamage(damage_list)

# Greedy > defense > aggressive > greedy

# Two main columns:
core = [x for x in heroes_list if x in (
    'Abaddon', 'Alchemist', 'Brewmaster', 'Bristleback', 'Chaos Knight', 'Doom', 'Dragon Knight', 'Huskar', 'Kunkka',
    'Legion Commander', 'Lifestealer', 'Lycan', 'Mars', 'Night Stalker', 'Slardar', 'Spirit Breaker',
    'Sven', 'Tiny', 'Wraith King', 'Anti-Mage', 'Arc Warden', 'Bloodseeker', 'Broodmother', 'Clinkz', 'Drow Ranger',
    'Ember Spirit', 'Faceless Void', 'Gyrocopter', 'Juggernaut', 'Lone Druid', 'Luna', 'Medusa', 'Meepo', 'Mirana',
    'Monkey King', 'Morphling', 'Centaur Warrunner',
    'Naga Siren', 'Pangolier', 'Phantom Assassin', 'Phantom Lancer', 'Razor', 'Riki', 'Shadow Fiend', 'Slark', 'Sniper',
    'Spectre', 'Templar Assassin', 'Terrorblade', 'Troll Warlord', 'Ursa', 'Viper', 'Weaver', 'Death Prophet',
    'Invoker', 'Leshrac', 'Lina', "Nature's Prophet", 'Necrophos', 'Outworld Destroyer', 'Queen of Pain', 'Silencer',
    'Storm Spirit', 'Tinker', 'Void Spirit', 'Windranger')]

utility = [x for x in heroes_list if x in (
    'Abaddon', 'Alchemist', 'Earthshaker', 'Io', 'Kunkka', 'Omniknight', 'Phoenix', 'Sand King', 'Snapfire',
    'Treant Protector', 'Underlord', 'Undying', 'Wraith King', 'Mirana', 'Naga Siren', 'Vengeful Spirit', 'Venomancer',
    'Ancient Apparition', 'Bane', 'Chen', 'Crystal Maiden', 'Dark Willow', 'Dazzle', 'Disruptor', 'Enchantress',
    'Grimstroke', 'Jakiro', 'Keeper of the Light', 'Leshrac', 'Lich', 'Lina', 'Lion', 'Ogre Magi', 'Oracle', 'Rubick',
    'Shadow Demon', 'Shadow Shaman', 'Silencer', 'Skywrath Mage', 'Visage', 'Warlock', 'Windranger', 'Winter Wyvern',
    'Witch Doctor'
)]

# 0.1 - Slow
# 0.3 - Simple stuns/other cc
# 0.5 - Silence or utility spells
# 0.7 - Control Through BKB
# 0.9 - AOE cc Through BKB

# Disable tier list (manually filled)
disable_tier = {
    '0.1': ['Abaddon', 'Io', 'Lifestealer', 'Bristleback', 'Lycan', 'Night Stalker', 'Omniknight',
            'Timbersaw', 'Undying', 'Arc Warden', 'Broodmother', 'Drow Ranger', 'Phantom Assassin',
            'Phantom Lancer', 'Razor', 'Spectre', 'Ursa', 'Venomancer', 'Viper', 'Dazzle', 'Death Prophet',
            'Keeper of the Light', "Nature's Prophet", 'Pugna', 'Queen of Pain'],
    '0.3': ['Alchemist', 'Brewmaster', 'Centaur Warrunner', 'Chaos Knight', 'Dragon Knight', 'Earth Spirit',
            'Earthshaker', 'Elder Titan', 'Kunkka', 'Mars', 'Pudge', 'Sand King', 'Slardar', 'Snapfire', 'Sven',
            'Tidehunter', 'Tiny', 'Underlord', 'Wraith King', 'Bounty Hunter', 'Ember Spirit', 'Gyrocopter', 'Hoodwink',
            'Luna', 'Meepo', 'Mirana', 'Monkey King', 'Nyx Assassin', 'Pangolier', 'Shadow Fiend', 'Slark', 'Sniper',
            'Terrorblade', 'Troll Warlord', 'Ancient Apparition', 'Chen', 'Crystal Maiden', 'Dark Willow', 'Invoker',
            'Jakiro', 'Leshrac', 'Lich', 'Lina', 'Lion', 'Ogre Magi', 'Oracle', 'Outworld Destroyer', 'Lone Druid',
            'Shadow Shaman', 'Storm Spirit', 'Techies', 'Visage', 'Void Spirit', 'Windranger', 'Witch Doctor', 'Zeus',
            'Riki'],
    '0.5': ['Bloodseeker', 'Morphling', 'Dark Seer', 'Disruptor', 'Enchantress', 'Grimstroke', 'Shadow Demon',
            'Skywrath Mage', 'Death Prophet'],
    '0.7': ['Beastmaster', 'Doom', 'Legion Commander', 'Tusk', 'Huskar', 'Anti-Mage', 'Naga Siren', 'Vengeful Spirit',
            'Bane', 'Batrider', 'Templar Assassin', 'Necrophos', 'Queen of Pain'],
    '0.9': ['Axe', 'Clockwerk', 'Magnus', 'Phoenix', 'Spirit Breaker', 'Treant Protector', 'Faceless Void', 'Medusa',
            'Enigma', 'Puck', 'Rubick', 'Silencer', 'Warlock', 'Winter Wyvern'],
}


def split_ranges(list_):
    return {
        '0.1': [x[1] for x in list_ if 0.1 < float(x[0]) < 0.3],
        '0.3': [x[1] for x in list_ if 0.5 > float(x[0]) >= 0.3],
        '0.5': [x[1] for x in list_ if 0.7 > float(x[0]) >= 0.5],
        '0.7': [x[1] for x in list_ if 0.9 > float(x[0]) >= 0.7],
        '0.9': [x[1] for x in list_ if float(x[0]) > 0.9]
    }


# Heal tier list
heal_tier = split_ranges(heal_list)
# Tower tier list
tower_tier = split_ranges(tower_list)
# Damage tier list
damage_tier = split_ranges(damage_list)
# Manually filled save list, save others and maybe oneself
# 0.1 - heal
# 0.3 - positioning
# 0.5 - astral, other stuff
# 0.7 - dispell, through bkb
# 0.9 - damage reduction, save from death, strong dispell
save_tier = {
    '0.1': ['Chen', 'Dark Seer', 'Enchantress', 'Juggernaut', 'Lifestealer', 'Terrorblade', 'Treant Protector',
            'Undying', 'Warlock', 'Witch Doctor', ''],
    '0.3': ['Earth Spirit', 'Earthshaker', 'Faceless Void', 'Grimstroke', 'Keeper of the Light', 'Kunkka', 'Lone Druid',
            'Lycan', 'Naga Siren', "Nature's Prophet", 'Puck', 'Sniper', 'Underlord', 'Vengeful Spirit', ''],
    '0.5': ['Bane', 'Morphling', 'Outworld Destroyer', 'Pugna', 'Rubick', 'Shadow Demon', 'Tusk', ''],
    '0.7': ['Alchemist', 'Chaos Knight', ''],
    '0.9': ['Arc Warden', 'Batrider', 'Centaur Warrunner', 'Dazzle', 'Abaddon', 'Io', 'Legion Commander', 'Lich',
            'Mars', 'Ogre Magi', 'Omniknight', 'Oracle', 'Phoenix', 'Pudge', 'Snapfire', 'Tinker', 'Weaver',
            'Winter Wyvern', 'Wraith King']
}


# Tryin to make last pick


class CounterSynergy:
    damage = 0
    heal = 0
    tower = 0
    disable = 0
    save = 0

    RANGES = [0.1, 0.3, 0.5, 0.7, 0.9]

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Hero: {self.name}\n' \
               f'Damage: {self.damage}\n' \
               f'Heal potential: {self.heal}\n' \
               f'Push potential: {self.tower}\n' \
               f'Disable potential: {self.disable}\n' \
               f'Save options: {self.save}\n'

    def counter(self):
        for i in CounterSynergy.RANGES:
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

        print(self, end='')


hero = CounterSynergy(input('Введите героя... '))

hero.counter()
