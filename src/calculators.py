from templates import Calculator


class OverallCalculator(Calculator):

    def __init__(self, first_team, second_team):
        self.first = first_team
        self.second = second_team

    def calculate(self):
        first_team_power = 0
        second_team_power = 0
        for hero in self.first:
            first_team_power += hero.damage + hero.heal + hero.tower + hero.disable + hero.save + hero.escape + hero.durable

        for hero in self.second:
            second_team_power += hero.damage + hero.heal + hero.tower + hero.disable + hero.save + hero.escape + hero.durable
        return OverallCalculatorResult(first_team_power, second_team_power)


class OverallCalculatorResult:
    def __init__(self, first_team_power, second_team_power):
        self.first_team_power = first_team_power
        self.second_team_power = second_team_power
        self.win_team = 'Вторая команда'
        if first_team_power > second_team_power:
            self.win_team = 'Первая команда'
        elif first_team_power == second_team_power:
            self.win_team = 'Обе команды хехе бой'

    def __str__(self):
        return f'''
        У первой команды: {self.first_team_power}
        У второй команды: {self.second_team_power}
        Победила команда: {self.win_team}
        '''


class DetailedCalculator(Calculator):
    def __init__(self, team):
        self.team = team

    def calculate(self):
        team_damage_potential = 0
        team_heal_potential = 0
        team_tower_potential = 0
        team_disable_potential = 0
        team_save_potential = 0
        team_escape_potential = 0
        team_durable_potential = 0
        for hero in self.team:
            team_damage_potential += hero.damage
            team_heal_potential += hero.heal
            team_tower_potential += hero.tower
            team_disable_potential += hero.disable
            team_save_potential += hero.save
            team_escape_potential += hero.escape
            team_durable_potential += hero.durable
        return DetailedCalculatorResult(team_damage_potential, team_heal_potential, team_tower_potential,
                                        team_disable_potential, team_save_potential, team_escape_potential,
                                        team_durable_potential)


class DetailedCalculatorResult:
    def __init__(self, team_damage, team_heal, team_tower, team_disable, team_save, team_escape, team_durable):
        self.team_damage = team_damage
        self.team_heal = team_heal
        self.team_tower = team_tower
        self.team_disable = team_disable
        self.team_save = team_save
        self.team_escape = team_escape
        self.team_durable = team_durable

    def __str__(self):
        return f'''
        This team damage potential   : {self.team_damage}
        While heal potential is      : {self.team_heal}
        Also push potential is       : {self.team_tower}
        And this team disables like  : {self.team_disable}
        Saves teammates or themselves: {self.team_save}
        Although escapes like this   : {self.team_escape}
        And lives in fight like      : {self.team_durable}
        '''
