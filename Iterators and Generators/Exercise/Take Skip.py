class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.times = 0
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.times >= self.count:
            raise StopIteration
        result = self.number
        self.number += self.step
        self.times += 1
        return result

numbers = take_skip(2, 6)
for number in numbers:
    print(number)