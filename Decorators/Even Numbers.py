import functools

def even_numbers(function):
    @functools.wraps(function)
    def wrapper(numbers):
        return [n for n in numbers if n % 2 == 0]
    # TODO: Implement
    return wrapper

@even_numbers
def get_numbers(numbers):
    return numbers
print(get_numbers([1, 2, 3, 4, 5]))
