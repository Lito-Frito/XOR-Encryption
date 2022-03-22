def decrypt(scrambled, ascii, iicsa, key):
    input("\nTo decrypt, we simply take the same 256-bit key we used to "
          "encrypt and run XOR again. This type of encryption is called "
          "symmetrical because the same key is used in encryption and "
          "decryption. In asymmetrical encryption, you'd use one key to,"
          "encrypt and another to decrypt. Now let's decrypt.")

    input("\nDecrypting...")
    decrypted = ''
    # Decrypt encrypted message by using XOR (^) again
    for k in range(len(scrambled)):
        decrypted += str(int(scrambled[k]) ^ int(key[k]))

    # create number of needed blocks again
    blocks = []
    for block in range(len(scrambled)//8):
        blocks.append('')

    # start filling out each byte with the decrypted binary (ASCII values)
    block = 0
    for letter in range(len(decrypted)):
        blocks[block] += decrypted[letter]

        # parse digits by bytes
        if len(blocks[block]) == 8:
            block += 1

    decrypted_message = ''
    input(f"\nHere's your message changed back to ASCII via binary: {blocks}")

    input("\nCompare them to the first bytes I showed you or an ASCII table "
          "to verify.")

    # Convert back to ASCII text
    for byte in range(len(blocks)):
        decrypted_message += iicsa[blocks[byte]]

    input("\nNow we'll convert these bits back into text.")

    input(f"\nYour decrypted message is: \"{decrypted_message}\"")

    input("\nUsing XOR in encryption is a common technique, but it's not "
          "enough on its own. This is because if you send enough messages, "
          "people can figure out your key through guess-and-checking.")

    input("\nOne way to counteract this is to use a different key for each "
          "message, but that soon starts to take up a lot of space. You can "
          "run this script again and it'll use a different key if you want to "
          "see how that changes things.")

    input("\nThat's it; I hope you learned something!")

    return
