def spin_words(sentence: str) -> str:
    # check if the parameter meets the string type requirements
    if not isinstance(sentence, str):
        return print('Only string objects are allowed!!')

    # split the string at every space
    split = sentence.split()

    # iterate the array
    for word in split:
        # check if the word length is greater or equal to 5
        if len(word) >= 5:
            # update the value of the word to its inverse
            split[split.index(word)] = word[::-1]

    # return the joined string
    return(' '.join(split))
