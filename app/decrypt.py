def pure_decrypt(scrambled, key, ascii, iicsa):
    decrypted_bin = ''.join(str(int(scrambled[i]) ^ int(key[i])) for i in range(len(scrambled)))
    blocks = [decrypted_bin[i:i+8] for i in range(0, len(decrypted_bin), 8)]
    decrypted_message = ''.join(iicsa[block] for block in blocks)
    return decrypted_message


def decrypt(scrambled, ascii, iicsa, key):
    input("\nTo decrypt, we simply take the same 256-bit key we used to "
          "encrypt and run XOR again. This type of encryption is called "
          "symmetrical because the same key is used in encryption and "
          "decryption. In asymmetrical encryption, you'd use one key to,"
          "encrypt and another to decrypt. Now let's decrypt.")

    input("\nDecrypting...")
    decrypted_bin = ''.join(str(int(scrambled[i]) ^ int(key[i])) for i in range(len(scrambled)))

    # create number of needed blocks again
    blocks = [decrypted_bin[i:i+8] for i in range(0, len(decrypted_bin), 8)]

    input(f"\nHere's your message changed back to ASCII via binary: {blocks}")

    input("\nCompare them to the first bytes I showed you or an ASCII table "
          "to verify.")

    # Convert back to ASCII text
    decrypted_message = pure_decrypt(scrambled, key, ascii, iicsa)

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
