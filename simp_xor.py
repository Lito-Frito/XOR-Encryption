import random
from textwrap import dedent

def encrypt(message, key, ascii, iicsa, keys):
    input("\nGreat! Let's change this into ASCII.")

    bin_string = ''
    scrambled = ''
    temp =  ''

    # Create bin version of message
    for i in range(len(message)):
        bin_string += ascii[message[i]]

    input(f"\nHere's your message translated to ASCII via binary: {bin_string}")
    print("\nIt's hard to parse out, so let's split this up by block/byte:")


    # Create blocks from bin_string
    ascii_blocks = []
    for block in range(len(bin_string)//8):
        ascii_blocks.append('')


    ascii_block = 0
    # Fill each block with the ASCII code
    for bit in range(len(bin_string)):
        ascii_blocks[ascii_block] += bin_string[bit]

        # Parse by byte
        if len(ascii_blocks[ascii_block]) == 8:
            ascii_block += 1

    input(f"Blocks: {ascii_blocks}")

    input("\nIf you look up a table for ASCII values in binary online, you'll "\
    "see that the bytes match the values for the letters you typed.")

    input("\nNow let's start encrypting.")

    input(f"\nWe'll use a 256-bit key with a value of {key}")
    print("\nWe'll use the XOR operation to encrypt.\nXOR only returns 1 if "\
    "the two bits it compares are different; otherwise it returns 0.")

    input("It compares the first bit from our encrypted message in binary "\
    f"(0) to the first bit in the key ({key[0]}) using XOR, and so on for every "\
    "bit.")

    # Create the encrypted string called 'scrambled'
    for j in range(len(bin_string)):
        scrambled += str(int(bin_string[j]) ^ int(key[j]))

    input(f"\nYour encrypted message is: {scrambled}")


    # create number of needed bytes
    bytes = []
    for num in range(len(scrambled)//8):
        bytes.append('')

    # Fill each byte
    byte = 0
    for bit in range(len(scrambled)):
        bytes[byte] += scrambled[bit]

        # parse by byte
        if len(bytes[byte]) == 8:
            byte += 1

    print(f"\nLet's look at it by byte: {bytes}")

    input("\nSee how these values are different than the ASCII binary values? "\
    "If we tried to convert back to ASCII, we get an error. That's because "\
    "what this generates is gibberish.")

    return scrambled


def decrypt(scrambled, ascii, iicsa, key, keys):
    input("\nTo decrypt, we simply take the same 256-bit key we used to "\
    "encrypt and run the XOR operation again. This type of encryption is called "\
    "symmetrical because the same key is used in encryption and decryption. Now "\
    "let's decrypt.")

    input("\nDecrypting...")
    reversed = ''
    # Decrypt encrypted message
    for k in range(len(scrambled)):
        reversed += str(int(scrambled[k]) ^ int(key[k]))

    # create number of needed blocks in array
    blocks = []
    for block in range(len(scrambled)//8):
        blocks.append('')

    # start filling out each byte of ascii binary
    block = 0
    for letter in range(len(reversed)):
        blocks[block] += reversed[letter]

        # parse digits by bytes
        if len(blocks[block]) == 8:
            block += 1

    decrypted_message = ''
    input(f"\nHere's your message changed back to ASCII via binary: {blocks}")

    input("\nCompare them to the first bytes I showed you or an ASCII table "\
    "to verify.")

    # Convert back to ASCII text
    for byte in range(len(blocks)) :
        decrypted_message += iicsa[blocks[byte]]

    input("\nNow we'll convert these bits back into text.")

    input(f"\nYour decrypted message is: \"{decrypted_message}\"")

    input("\nUsing XOR in encryption is a common technique, but it's not "\
    "enough on its own. This is because if you send enough messages, people "\
    "can figure out your key.")

    input("\nOne way to counteract this is to use a different key for each "\
    "message, but that soon starts to take up a lot of space. You can run  "\
    "this script again and it'll use a different key if you want to see how  "\
    "that changes things.")

    input("\nThat's it; hope you learned something!")

    return

def block_cipher():
    # Create ASCII table in binary
    ascii = {
    'a' : '01100001',
    'b' : '01100010',
    'c' : '01100011',
    'd' : '01100100',
    'e' : '01100101',
    'f' : '01100110',
    'g' : '01100111',
    'h' : '01101000',
    'i' : '01101001',
    'j' : '01101010',
    'k' : '01101011',
    'l' : '01101100',
    'm' : '01101101',
    'n' : '01101110',
    'o' : '01101111',
    'p' : '01110000',
    'q' : '01110001',
    'r' : '01110010',
    's' : '01110011',
    't' : '01110100',
    'u' : '01110101',
    'v' : '01110110',
    'w' : '01110111',
    'x' : '01111000',
    'y' : '01111001',
    'z' : '01111010',
    '.' : '00101110',
    ' ' : '00100000',
    '!' : '00100001',
    '?' : '00111111',
    '\'' : '00100111',
    '"' : '00100010',
    '0' : '00110000',
    '1' : '00110001',
    '2' : '00110010',
    '3' : '00110011',
    '4' : '00110100',
    '5' : '00110101',
    '6' : '00110110',
    '7' : '00110111',
    '8' : '00111000',
    '9' : '00111001',
    'A' : '01000001',
    'B' : '01000010',
    'C' : '01000011',
    'D' : '01000100',
    'E' : '01000101',
    'F' : '01000110',
    'G' : '01000111',
    'H' : '01001000',
    'I' : '01001001',
    'J' : '01001010',
    'K' : '01001011',
    'L' : '01001100',
    'M' : '01001101',
    'N' : '01001110',
    'O' : '01001111',
    'P' : '01010000',
    'Q' : '01010001',
    'R' : '01010010',
    'S' : '01010011',
    'T' : '01010100',
    'U' : '01010101',
    'V' : '01010110',
    'W' : '01010111',
    'X' : '01011000',
    'Y' : '01011001',
    'Z' : '01011010'
    }

    # Reverse key:value pairs in ascii{}
    iicsa = dict([(value, key) for key, value in ascii.items()])

    input("Welcome! This is a tool to help people understand a simple "\
    "encryption technique called XOR.")

    ok_length = True
    while ok_length:
        phrase = input("Type a message that has 32 characters or less using "\
        "letters, numbers, or basic punctuation: ")
        if len(phrase) > 32:
            print("\nThat's too long; make sure it's less than 32 characters.")

        else:
            ok_length = False

    keys = ['1111' * 64,
    '0000' * 64,
    '1010' * 64,
    '0101' * 64,
    '1010' * 64,
    '1001' * 64,
    '0011' * 64,
    '1100' * 64]

    key = keys[random.randint(1,7)]

    # 01101000011010010110100001101001 is HIHI
    # key = 11111111111111111111111111111111
    # XOR = 10010111100101101001011110010110

    scrambled = encrypt(phrase, key, ascii, iicsa, keys)
    decrypt(scrambled, ascii, iicsa, key, keys)

block_cipher()
