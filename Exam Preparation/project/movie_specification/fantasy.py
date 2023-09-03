from movie_specification.movie import Movie
from user import User

# TODO: Не забравяй да смениш import имената с project.user, защото Judge няма да го приеме


class FantasyMovie(Movie):
    def __init__(self, title: str, year: int, owner: User, age_restriction: int = 6):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < 6:
            raise ValueError("Fantasy movies must be restricted for audience under 6 years!")
        self.__age_restriction = value

    def details(self):
        return f"Fantasy - Title:{self.title}, Year:{self.year}," \
               f" Age restriction:{self.age_restriction}," \
               f" Likes:{self.likes}," \
               f" Owned by:{self.owner}"
