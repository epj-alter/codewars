# Define the function and the parameter types it accepts for clear use
def square_digits(num: int) -> int:
    # check if the parameter meets the type expectations
    if not isinstance(num, int):
        return print('Only intergers are allowed!')

    # create a list to hold each squared number
    numlist = []
    # cast the number received to a string in order to iterate through it
    numstring = str(num)

    # iterate through each number and do number²
    for number in numstring:
        numlist.append(str(int(number) ** 2))

    # join the array of strings and cast to am interger in order to return
    return int(''.join(numlist))
