class OverallCalculator:

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
        if first_team_power < second_team_power:
            self.win_team = 'Первая команда'
        elif first_team_power == second_team_power:
            self.win_team = 'Обе команды хехе бой'

    def __str__(self):
        return f'''
        У первой команды: {self.first_team_power}
        У второй команды: {self.second_team_power}
        Победила команда: {self.win_team}
        '''


