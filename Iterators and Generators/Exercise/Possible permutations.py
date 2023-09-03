from itertools import permutations


def possible_permutations(lst):
    for perm in permutations(lst):
        yield list(perm)


[print(n) for n in possible_permutations([1, 2, 3])]

