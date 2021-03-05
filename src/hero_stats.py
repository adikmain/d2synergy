from src.parser_ import get_heroes, get_timers

# Main lists
heroes_list = []
heal_list = []
tower_list = []
damage_list = []
timers_list = []
# info = [[y.text for y in x[1:]] for x in get_heroes()]

info = [x for x in get_heroes()]
timers = [x for x in get_timers()]


# Names list
def getHeroes(names):
    for i in range(len(info)):
        names.append(info[i][0])


getHeroes(heroes_list)


# Heal tier list

def getHeal(heroes):
    for i in range(len(info)):
        heroes.append([float(info[i][3]), info[i][0]])
    top_heal = max(heroes)[0]
    for v in range(len(heal_list)):
        heal_list[v][0] /= top_heal


getHeal(heal_list)


# Tower damage tier list

def getTower(heroes):
    for i in range(len(info)):
        heroes.append([float(info[i][2]), info[i][0]])
    top_tower = max(heroes)[0]
    for v in range(len(heroes)):
        heroes[v][0] /= top_tower


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


# Timers tier list

def getTimers(heroes):
    for i in range(len(timers)):
        heroes.append([float(timers[i][1][:2]), timers[i][0]])
    for v in range(len(heroes)):
        if heroes[v][0] > 42.6:
            heroes[v][0] = 0.9
        elif heroes[v][0] > 39.8:
            heroes[v][0] = 0.7
        elif heroes[v][0] > 38.4:
            heroes[v][0] = 0.5
        elif heroes[v][0] > 37:
            heroes[v][0] = 0.3
        else:
            heroes[v][0] = 0.1


# 37 - 44 : 1.4 step : 37 - 38.4, 38.4 - 39.8, 39.8 - 41.2, 42.6 - 44.0

getTimers(timers_list)

# Greedy > defense > aggressive > greedy

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
        '0.1': [x[1] for x in list_ if 0.1 <= float(x[0]) < 0.3],
        '0.3': [x[1] for x in list_ if 0.5 > float(x[0]) >= 0.3],
        '0.5': [x[1] for x in list_ if 0.7 > float(x[0]) >= 0.5],
        '0.7': [x[1] for x in list_ if 0.9 > float(x[0]) >= 0.7],
        '0.9': [x[1] for x in list_ if float(x[0]) >= 0.9]
    }


# Heal tier list
heal_tier = split_ranges(heal_list)
# Tower tier list
tower_tier = split_ranges(tower_list)
# Damage tier list
damage_tier = split_ranges(damage_list)
# Timers tier list
timers_list = split_ranges(timers_list)
# Manually filled save list, save others and maybe oneself
# 0.1 - heal
# 0.3 - positioning
# 0.5 - astral, other stuff
# 0.7 - dispell, through bkb
# 0.9 - damage reduction, save from death, strong dispell
save_tier = {
    '0.1': ['Dark Seer', 'Enchantress', 'Juggernaut', 'Lifestealer', 'Terrorblade', 'Treant Protector',
            'Undying', 'Warlock', 'Witch Doctor'],
    '0.3': ['Earth Spirit', 'Earthshaker', 'Faceless Void', 'Grimstroke', 'Keeper of the Light', 'Kunkka', 'Lone Druid',
            'Lycan', 'Naga Siren', "Nature's Prophet", 'Puck', 'Sniper', 'Underlord', 'Vengeful Spirit'],
    '0.5': ['Chen', 'Bane', 'Morphling', 'Outworld Destroyer', 'Pugna', 'Rubick', 'Shadow Demon', 'Tusk'],
    '0.7': ['Alchemist', 'Chaos Knight'],
    '0.9': ['Arc Warden', 'Batrider', 'Centaur Warrunner', 'Dazzle', 'Abaddon', 'Io', 'Legion Commander', 'Lich',
            'Mars', 'Ogre Magi', 'Omniknight', 'Oracle', 'Phoenix', 'Pudge', 'Snapfire', 'Tinker', 'Weaver',
            'Winter Wyvern', 'Wraith King']
}

# Manually filled escape tier, options(spells) to escape and survive
# 0.1 - bad escape but has
# 0.3 - invisibility
# 0.5 - can escape many times
# 0.7 - make escape others and oneself
# 0.9 - god of escape
escape_tier = {
    '0.1': ['Slardar', 'Arc Warden', 'Hoodwink', 'Grimstroke'],
    '0.3': ['Treant Protector', 'Bounty Hunter', 'Broodmother', 'Clinkz', 'Faceless Void', 'Nyx Assassin', 'Invoker',
            'Windranger', 'Visage', 'Brewmaster'],
    '0.5': ['Lifestealer', 'Sand King', 'Spirit Breaker', 'Timbersaw', 'Anti-Mage', 'Meepo', 'Juggernaut', 'Meepo',
            'Monkey King', 'Morphling', 'Pangolier', 'Phantom Assassin', 'Phantom Lancer', 'Riki', 'Slark', 'Spectre',
            'Templar Assassin', 'Batrider', 'Dark Willow', 'Queen of Pain', 'Lone Druid', 'Rubick'],
    '0.7': ['Centaur Warrunner', 'Earth Spirit', 'Io', 'Lycan', 'Snapfire', 'Underlord', 'Mirana', 'Naga Siren',
            'Vengeful Spirit', 'Weaver', 'Dark Seer', 'Oracle'],
    '0.9': ['Ember Spirit', "Nature's Prophet", 'Puck', 'Storm Spirit', 'Void Spirit']
}
# 0.1 - stats
# 0.3 - skills
# 0.5 - stats + skills
# 0.7 - heal
# 0.9 - hard to kill
durable_tier = {
    '0.1': ['Beastmaster', 'Chaos Knight', 'Clockwerk', 'Ogre Magi'],
    '0.3': ['Axe', 'Doom', 'Treant Protector', 'Bane', 'Visage'],
    '0.5': ['Dragon Knight', 'Earth Spirit', 'Elder Titan', 'Lycan', 'Mars', 'Night Stalker', 'Pudge', 'Slardar',
            'Spirit Breaker', 'Sven', 'Tidehunter', 'Tiny', 'Underlord', 'Undying', 'Faceless Void', 'Pangolier',
            'Razor', 'Viper'],
    '0.7': ['Abaddon', 'Alchemist', 'Huskar', 'Kunkka', 'Legion Commander', 'Lifestealer', 'Timbersaw', 'Lone Druid',
            'Morphling', 'Necrophos'],
    '0.9': ['Brewmaster', 'Bristleback', 'Centaur Warrunner', 'Omniknight', 'Wraith King', 'Medusa', 'Spectre',
            'Troll Warlord', 'Ursa', 'Enchantress']
}

