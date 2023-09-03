from typing import List, Optional
from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    def __init__(self, name: str, capacity: int):
        if not name.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    def add_equipment(self, equipment_type: str):
        if equipment_type not in ['KneePad', 'ElbowPad']:
            raise Exception("Invalid equipment type!")

        if equipment_type == 'KneePad':
            equipment = KneePad()
        else:
            equipment = ElbowPad()

        self.equipment.append(equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type == "OutdoorTeam":
            team = OutdoorTeam(team_name, country, advantage)
        elif team_type == "IndoorTeam":
            team = IndoorTeam(team_name, country, advantage)
        else:
            raise Exception("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        self.teams.append(team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = next(
            (eq for eq in self.equipment if isinstance(eq, KneePad if equipment_type == 'KneePad' else ElbowPad)), None)
        team = next((tm for tm in self.teams if tm.name == team_name), None)

        if not equipment or not team:
            raise Exception("Equipment or team not found.")

        if equipment.price > team.budget:
            raise Exception("Budget is not enough!")

        team.budget -= equipment.price
        team.equipment.append(equipment)
        self.equipment.remove(equipment)
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        for team in self.teams:
            if team.name == team_name:
                break
        else:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        equipment_list = [eq for eq in self.equipment if
                          isinstance(eq, KneePad if equipment_type == 'KneePad' else ElbowPad)]

        for equipment in equipment_list:
            equipment.increase_price()

        return f"Successfully changed {len(equipment_list)}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = next((tm for tm in self.teams if tm.name == team_name1), None)
        team2 = next((tm for tm in self.teams if tm.name == team_name2), None)

        if not team1 or not team2:
            raise Exception("Teams not found.")

        if isinstance(team1, OutdoorTeam) and isinstance(team2, IndoorTeam):
            raise Exception("Game cannot start! Team types mismatch!")
        elif isinstance(team1, IndoorTeam) and isinstance(team2, OutdoorTeam):
            raise Exception("Game cannot start! Team types mismatch!")

        team1_score = team1.advantage + sum(eq.protection for eq in team1.equipment)
        team2_score = team2.advantage + sum(eq.protection for eq in team2.equipment)

        if team1_score > team2_score:
            team1.win()
            winner = team1
        elif team2_score > team1_score:
            team2.win()
            winner = team2
        else:
            return "No winner in this game."

        return f"The winner is {winner.name}."

    def get_statistics(self):
        self.teams.sort(key=lambda x: x.wins, reverse=True)
        teams_stats = '\n'.join([team.get_statistics() for team in self.teams])

        return f"Tournament: {self.name}\n" \
               f"Number of Teams: {len(self.teams)}\n" \
               f"Teams:\n{teams_stats}"


t = Tournament('SoftUniada2023', 2)

print(t.add_equipment('KneePad'))
print(t.add_equipment('ElbowPad'))

print(t.add_team('OutdoorTeam', 'Levski', 'BG', 250))
print(t.add_team('OutdoorTeam', 'Spartak', 'BG', 250))
print(t.add_team('IndoorTeam', 'Dobrich', 'BG', 280))

print(t.sell_equipment('KneePad', 'Spartak'))

print(t.remove_team('Levski'))
print(t.add_team('OutdoorTeam', 'Lokomotiv', 'BG', 250))

print(t.increase_equipment_price('ElbowPad'))
print(t.increase_equipment_price('KneePad'))

print(t.play('Lokomotiv', 'Spartak'))

print(t.get_statistics())
