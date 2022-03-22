import random
from encrypt import encrypt
from decrypt import decrypt


def block_cipher():
    # Create ASCII table in binary
    ascii = {
        'a': '01100001',
        'b': '01100010',
        'c': '01100011',
        'd': '01100100',
        'e': '01100101',
        'f': '01100110',
        'g': '01100111',
        'h': '01101000',
        'i': '01101001',
        'j': '01101010',
        'k': '01101011',
        'l': '01101100',
        'm': '01101101',
        'n': '01101110',
        'o': '01101111',
        'p': '01110000',
        'q': '01110001',
        'r': '01110010',
        's': '01110011',
        't': '01110100',
        'u': '01110101',
        'v': '01110110',
        'w': '01110111',
        'x': '01111000',
        'y': '01111001',
        'z': '01111010',
        '.': '00101110',
        ' ': '00100000',
        '!': '00100001',
        '?': '00111111',
        '\\': '01011100',
        '/': '00101111',
        '\'': '00100111',
        '"': '00100010',
        '0': '00110000',
        '1': '00110001',
        '2': '00110010',
        '3': '00110011',
        '4': '00110100',
        '5': '00110101',
        '6': '00110110',
        '7': '00110111',
        '8': '00111000',
        '9': '00111001',
        'A': '01000001',
        'B': '01000010',
        'C': '01000011',
        'D': '01000100',
        'E': '01000101',
        'F': '01000110',
        'G': '01000111',
        'H': '01001000',
        'I': '01001001',
        'J': '01001010',
        'K': '01001011',
        'L': '01001100',
        'M': '01001101',
        'N': '01001110',
        'O': '01001111',
        'P': '01010000',
        'Q': '01010001',
        'R': '01010010',
        'S': '01010011',
        'T': '01010100',
        'U': '01010101',
        'V': '01010110',
        'W': '01010111',
        'X': '01011000',
        'Y': '01011001',
        'Z': '01011010'
    }

    # Reverse key:value pairs in ascii{}
    iicsa = dict([(value, key) for key, value in ascii.items()])

    input("Welcome! This is a tool to help people understand a simple "
          "encryption technique called XOR.")

    not_ok_length = True
    while not_ok_length:
        phrase = input("Type a message that has 32 characters or less using "
                       "letters, numbers, or basic punctuation: ")
        if len(phrase) > 32:
            print("\nThat's too long; make sure it's less than 32 characters.")

        else:
            not_ok_length = False

    keys = ['1111' * 64,
            '0000' * 64,
            '1010' * 64,
            '0101' * 64,
            '0110' * 64,
            '1001' * 64,
            '0011' * 64,
            '1100' * 64]

    key = keys[random.randint(0, 7)]

    scrambled = encrypt(phrase, key, ascii, iicsa)
    decrypt(scrambled, ascii, iicsa, key)


block_cipher()
