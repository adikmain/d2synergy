from hero import Hero
from hero_stats import heroes_list
from overall_calculator import OverallCalculator

if __name__ == '__main__':
    team1: list = ['Phantom Lancer', 'Ancient Apparition', 'Zeus', 'Bounty Hunter', 'Dark Seer']
    team2: list = ['Disruptor', 'Wraith King', 'Sniper', 'Nyx Assassin', 'Axe']

    heroes = {hero_name: Hero(hero_name) for hero_name in sorted(heroes_list)}

    calculator = OverallCalculator([heroes[hero_name] for hero_name in team1],
                                   [heroes[hero_name] for hero_name in team2])
    print(calculator.calculate())
    print(heroes['Zeus'].damage)


