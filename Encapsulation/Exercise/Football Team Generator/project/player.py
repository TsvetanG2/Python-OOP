class Player:

    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        self.__name = name #Private
        self.__sprint = sprint #Private
        self.__dribble = dribble #Private
        self.__passing = passing #Private
        self.__shooting = shooting #Private

    @property
    def name(self) -> str: #Имаме property само по име по условие, Връща str
        return self.__name

    def __str__(self) -> str:
        return f"Player: {self.name}\n" \
               f"Sprint: {self.__sprint}\n" \
               f"Dribble: {self.__dribble}\n" \
               f"Passing: {self.__passing}\n" \
               f"Shooting: {self.__shooting}"