def xo(s: str) -> str:
    # Quantify the we want to check letters
    o_qtty = 0
    x_qtty = 0

    # Iterate lowercased input to check all matches
    for letter in s.lower():
        if letter == "o":
            o_qtty += 1
        if letter == "x":
            x_qtty += 1
    # Return comparison between both letter quantities.
    return x_qtty == o_qtty
