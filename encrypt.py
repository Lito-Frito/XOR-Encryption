def encrypt(message, key, ascii, iicsa):
    input("\nGreat! Let's change this into ASCII.")

    bin_string = ''
    scrambled = ''

    # Create binary version of message
    for letter in range(len(message)):
        bin_string += ascii[message[letter]]

    input(
        f"\nHere's your message translated from ASCII to binary: {bin_string}")
    print("\nIt's hard to parse out, so let's split this up by block/byte:")

    # Create empty blocks based off size of bin_string
    ascii_blocks = []
    for block in range(len(bin_string)//8):
        ascii_blocks.append('')

    # Start with first block and then fill each block with the binary output
    ascii_block = 0
    for bit in range(len(bin_string)):
        ascii_blocks[ascii_block] += bin_string[bit]

        # Parse by byte (i.e. move onto next block every 8 bits)
        if len(ascii_blocks[ascii_block]) == 8:
            ascii_block += 1

    input(f"Blocks: {ascii_blocks}")

    input("\nLet's look up a table for ASCII values in binary and print out "
          "their values by character; you'll see that the bytes match the "
          "values for the letters you typed.\n")

    # Print each character from message in ASCII and binary alonside each other
    for char in message:
        print(char, ascii[char])

    input("\nNow let's start encrypting.")

    input(f"\nWe'll use a 256-bit key with a value of {key}")
    
    print("\nWe'll use the XOR operation to encrypt.\nXOR only returns 1 if "
          "the two bits it compares are different; otherwise it returns 0.")

    input("It compares the first bit from our message that's in binary "
          f"(0) to the first bit in the key ({key[0]}) using XOR, "
          "for every bit.")

    # Create the encrypted string called 'scrambled'
    for bit in range(len(bin_string)):
        scrambled += str(int(bin_string[bit]) ^ int(key[bit]))

    input(f"\nYour encrypted message is: {scrambled}")

    # create number of needed bytes (unit of 8 bits)
    bytes = []
    for bit in range(len(scrambled)//8):
        bytes.append('')

    # Fill each byte, same as before
    byte = 0
    for bit in range(len(scrambled)):
        bytes[byte] += scrambled[bit]

        # parse by byte
        if len(bytes[byte]) == 8:
            byte += 1

    print(f"\nLet's look at it by byte: {bytes}")

    input("\nSee how these values are different than the ASCII binary values? "
          "If we tried to convert back to ASCII, we get an error. That's "
          "because what this generates is gibberish.")

    return scrambled
