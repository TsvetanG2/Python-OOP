def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                print(func(*args, **kwargs))
        return wrapper

    return decorator


@repeat(2)
def hi(name):
    return f"Hi, my name is {name}"


print(hi("Slim Shady"))
