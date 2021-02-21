from hero_stats import durable_tier, damage_tier, disable_tier, tower_tier, heal_tier, save_tier, \
    escape_tier


class Hero:
    damage = 0
    heal = 0
    tower = 0
    disable = 0
    save = 0
    escape = 0
    durable = 0

    RANGES = [0.1, 0.3, 0.5, 0.7, 0.9]

    def __init__(self, name):
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
               f'Hero durability: {self.durable}'

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


