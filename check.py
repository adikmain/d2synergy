import itertools
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
            'Shadow Shaman', 'Storm Spirit', 'Techies', 'Visage', 'Void Spirit', 'Windranger', 'Witch Doctor', 'Zeus'],
    '0.5': ['Bloodseeker', 'Morphling', 'Dark Seer', 'Disruptor', 'Enchantress', 'Grimstroke', 'Shadow Demon',
            'Skywrath Mage'],
    '0.7': ['Beastmaster', 'Doom', 'Legion Commander', 'Tusk', 'Huskar', 'Anti-Mage', 'Naga Siren', 'Vengeful Spirit',
            'Bane', 'Batrider', 'Templar Assassin', 'Necrophos', 'Queen of Pain'],
    '0.9': ['Axe', 'Clockwerk', 'Magnus', 'Phoenix', 'Spirit Breaker', 'Treant Protector', 'Faceless Void', 'Medusa',
            'Enigma', 'Puck', 'Rubick', 'Silencer', 'Warlock', 'Winter Wyvern'],
}


hero = "Nature's Prophet"

new_list = list(disable_tier.values())

a = itertools.chain.from_iterable(new_list)
print(hero in a)