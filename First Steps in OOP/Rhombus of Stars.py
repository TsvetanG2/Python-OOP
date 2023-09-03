def print_row(n, count):
    print(' ' * (n - count), end='')
    print(*['*'] * count)


def print_reversed_triangle(n):
    for count in range(n - 1, 0, - 1):
        print_row(n, count)


def print_rhomb(n):
    # Example No2 with Function
    for count in range(1, n + 1):
        print_row(n, count)

    for count in range(n - 1, 0, -1):
        print_row(n, count)


def print_square(n):
    for _ in range(n):
        print_row(n, n)


n = int(input())

#Example No1
#for count in range(1, n + 1):
    #print(' ' * (n - count), end='')
    #print(*['*'] * count)


#for count in range(n - 1, 0, -1):
    #print(' ' * (n - count), end='')
    #print(*['*'] * count)

print_rhomb(n)
