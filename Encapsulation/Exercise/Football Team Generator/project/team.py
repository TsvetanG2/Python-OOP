from typing import List, Union
from project.player import Player


class Team:

    def __init__(self, name: str, rating: int) -> None: #Връща нищо
        self.__name = name #Private
        self.__rating = rating #Private
        self.__players: List[Player] = []

    def add_player(self, player: Player) -> str: #Връщаме съобщения значи стринг
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str) -> Union[str, Player]: #Или връщаме стринг или Player
        try:
            player = [p for p in self.__players if p.name == player_name][0]#Връщаме играчите, на които имената са равни на плейр
            self.__players.remove(player)
            return player
        except IndexError:
            return f"Player {player_name} not found"

