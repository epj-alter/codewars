def accum(s: str) -> str:
    # check if string is valid [a-z, A-Z]
    if not s.isalpha():
        return 'Only alpha characters are allowed!'
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
