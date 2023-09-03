from typing import List
from project.equipment.base_equipment import BaseEquipment
from abc import ABC, abstractmethod


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float, wins: int = 0) -> None:
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget= budget
        self.wins = wins
        self.equipment: List[BaseEquipment] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    def win(self):
        pass

    def get_statistics(self):
        total_equipment_price = 0
        total_protection = 0

        for equip in self.equipment:
            total_equipment_price += equip.price
            total_protection += equip.protection

        avg_protection = total_protection // len(self.equipment) if self.equipment else 0

        return f"Name: {self.name}\n" \
               f"Country: {self.country}\n" \
               f"Advantage: {self.advantage} points\n" \
               f"Budget: {self.budget:.2f}EUR\n" \
               f"Wins: {self.wins}\n" \
               f"Total Equipment Price: {total_equipment_price:.2f}\n" \
               f"Average Protection: {avg_protection}"

