from abc import ABC, abstractmethod


class Shapes(ABC):

    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shapes):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def calculate_area(self):
        return self.width * self.height


class Triangle(Shapes):
    def __init__(self, side, height):
        self.side = side
        self.height = height

    @property
    def calculate_area(self):
        return (self.side / 2) * self.height


class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    @property
    def calculate_area(self):
        return 3.14 * (self.radius ** 2)


class AreaCalculator:

    def __init__(self, shapes):

        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calculate_area

        return total


shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
