import re


def to_camel_case(text: str) -> str:
    if not len(text) > 0:
        return ''
    # use regular expression to splice the string
    composites = re.split('[\W,-,_]', text)

    # use the str.title() method in all the composite words except the first one and return the new text
    return composites[0] + ''.join(x.title() for x in composites[1:])
