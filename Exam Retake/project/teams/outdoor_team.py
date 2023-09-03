from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    def __init__(self, name: str, country: str, advantage: int, budget: float = 1000.0, wins: int = 0,):
        super().__init__(name, country, advantage, budget, wins)

    def win(self):
        self.advantage += 115
        self.wins += 1
