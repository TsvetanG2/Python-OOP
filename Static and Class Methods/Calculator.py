from functools import reduce


#reduce - приема sequence - Taка изглежда един reduce = reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
#Това е ламбда функция. в първият аргумент подаваме как да се извърши даденото дейстиве - reduce(lambda x, y: x+y)
#Вторият аргумент е листа от числата върху които искаме да се извърши даденото действие - [1, 2, 3, 4, 5]

class Calculator:

    def __init__(self):
        return

    @staticmethod
    def add(*args):
        return reduce(lambda x, y: x + y, args)

    @staticmethod
    def multiply(*args):
        return reduce(lambda x, y: x * y, args)

    @staticmethod
    def divide(*args):
        return reduce(lambda x, y: x / y, args)

    @staticmethod
    def subtract(*args):
        return reduce(lambda x, y: x - y, args)


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))