import functools


def persistence(n):
    iterations = 0

    while n > 9:
        n = functools.reduce(lambda x, y: x * y, [int(i) for i in str(n)])
        iterations += 1

    return iterations
