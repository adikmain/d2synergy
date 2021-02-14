from main import heroes as info

# Main lists
heroes_list = []
heal_list = []
tower_list = []
damage_list = []


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
# Heal tier list
heal_tier = {
    '0.1': [x[1] for x in heal_list if 0.1 < float(x[0]) < 0.3],
    '0.3': [x[1] for x in heal_list if 0.5 > float(x[0]) >= 0.3],
    '0.5': [x[1] for x in heal_list if 0.7 > float(x[0]) >= 0.5],
    '0.7': [x[1] for x in heal_list if 0.9 > float(x[0]) >= 0.7],
    '0.9': [x[1] for x in heal_list if float(x[0]) > 0.9]
}
# Tower tier list
tower_tier = {
    '0.1': [x[1] for x in tower_list if 0.1 < float(x[0]) < 0.3],
    '0.3': [x[1] for x in tower_list if 0.5 > float(x[0]) >= 0.3],
    '0.5': [x[1] for x in tower_list if 0.7 > float(x[0]) >= 0.5],
    '0.7': [x[1] for x in tower_list if 0.9 > float(x[0]) >= 0.7],
    '0.9': [x[1] for x in tower_list if float(x[0]) > 0.9]

}
# Damage tier list
damage_tier = {
    '0.1': [x[1] for x in damage_list if 0.1 < float(x[0]) < 0.3],
    '0.3': [x[1] for x in damage_list if 0.5 > float(x[0]) >= 0.3],
    '0.5': [x[1] for x in damage_list if 0.7 > float(x[0]) >= 0.5],
    '0.7': [x[1] for x in damage_list if 0.9 > float(x[0]) >= 0.7],
    '0.9': [x[1] for x in damage_list if float(x[0]) > 0.9]
}

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

    def __init__(self, name):
        self.name = name

    def counter(self):
        print(f'Hero: {self.name}')
        if self.name in damage_tier['0.1']:
            self.damage += 0.1
        elif self.name in damage_tier['0.3']:
            self.damage += 0.3
        elif self.name in damage_tier['0.5']:
            self.damage += 0.5
        elif self.name in damage_tier['0.7']:
            self.damage += 0.7
        elif self.name in damage_tier['0.9']:
            self.damage += 0.9

        print(f'Damage: {self.damage}')

        if self.name in heal_tier['0.1']:
            self.heal += 0.1
        elif self.name in heal_tier['0.3']:
            self.heal += 0.3
        elif self.name in heal_tier['0.5']:
            self.heal += 0.5
        elif self.name in heal_tier['0.7']:
            self.heal += 0.7
        elif self.name in heal_tier['0.9']:
            self.heal += 0.9

        print(f'Heal potential: {self.heal}')

        if self.name in tower_tier['0.1']:
            self.tower += 0.1
        elif self.name in tower_tier['0.3']:
            self.tower += 0.3
        elif self.name in tower_tier['0.5']:
            self.tower += 0.5
        elif self.name in tower_tier['0.7']:
            self.tower += 0.7
        elif self.name in tower_tier['0.9']:
            self.tower += 0.9

        print(f'Push potential: {self.tower}')

        if self.name in disable_tier['0.1']:
            self.disable += 0.1
        elif self.name in disable_tier['0.3']:
            self.disable += 0.3
        elif self.name in disable_tier['0.5']:
            self.disable += 0.5
        elif self.name in disable_tier['0.7']:
            self.disable += 0.7
        elif self.name in disable_tier['0.9']:
            self.disable += 0.9

        print(f'Disable potential: {self.disable}')

        if self.name in save_tier['0.1']:
            self.save += 0.1
        elif self.name in save_tier['0.3']:
            self.save += 0.3
        elif self.name in save_tier['0.5']:
            self.save += 0.5
        elif self.name in save_tier['0.7']:
            self.save += 0.7
        elif self.name in save_tier['0.9']:
            self.save += 0.9

        print(f'Save options: {self.save}')


hero = CounterSynergy(input('Введите героя... '))

hero.counter()
