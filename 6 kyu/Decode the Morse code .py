# Delete this list
MORSE_CODE = []


def decodeMorse(morse_code):
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morse_code.strip().split('   '))
