from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    def __init__(self, name: str, country: str, advantage: int, budget: float = 500.0, wins: int = 0,):
        super().__init__(name, country, advantage, budget, wins)

    def win(self):
        self.advantage += 145
        self.wins += 1
