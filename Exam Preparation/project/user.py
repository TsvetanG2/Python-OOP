from typing import List
from movie_specification.movie import Movie


class User:
    def __init__(self, username: str, age: int) -> None:
        self.username = username
        self.age = age
        self.movies_liked: List[Movie] = []
        self.movies_owned: List[Movie] = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value == '':
            raise ValueError('Invalid username!')
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:  #Ако е под 6 годишна възраст
            raise ValueError('Users under the age of 6 are not allowed!')
        self.__age = value

    def __str__(self):
        result = f"Username {self.username}, Age: {self.age}\n"
        result += "Liked movies:\n"

        if not self.movies_liked:
            result += "No movies liked.\n"
        else:
            result += "\n".join([m.details() for m in self.movies_liked]) + "\n"

        result += "Owned movies: \n"

        if not self.movies_owned:
            result += "No movies owned.\n"
        else:
            result += "\n".join([m.details() for m in self.movies_owned]) + "\n"

        return result
