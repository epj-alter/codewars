def iq_test(numbers):
    mylist = [[numbers.split().index(x) for x in numbers.split() if int(x) % 2 == 0], [
        numbers.split().index(x) for x in numbers.split() if int(x) % 2 != 0]]
    return next(x[0] + 1 for x in mylist if len(x) <= 1)
