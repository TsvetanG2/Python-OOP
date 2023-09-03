def solution():
    def integers():
        num = 1
        while True:
            yield num
            num += 1
    # TODO: Implement
    def halves():
        for num in integers():
            yield num / 2
    # TODO: Implement
    def take(n, seq):
        result = []
        for _ in range(n):
            result.append(next(seq))
        return result
    # TODO: Implement
    return (take, halves, integers)

take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
