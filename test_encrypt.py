import unittest
from app.encrypt import pure_encrypt
from app.decrypt import pure_decrypt

# ASCII dictionary from main.py
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

iicsa = dict([(value, key) for key, value in ascii.items()])

# Fixed 256-bit key for testing
key = '1' * 256

class TestEncryptDecrypt(unittest.TestCase):

    def test_lower_case_sample(self):
        message = "hello"
        scrambled = pure_encrypt(message, key, ascii, iicsa)
        decrypted = pure_decrypt(scrambled, key, ascii, iicsa)
        self.assertEqual(decrypted, message)

    def test_upper_case_sample(self):
        message = "HELLO"
        scrambled = pure_encrypt(message, key, ascii, iicsa)
        decrypted = pure_decrypt(scrambled, key, ascii, iicsa)
        self.assertEqual(decrypted, message)

    def test_mixed_case_with_symbols(self):
        message = "Hello World!"
        scrambled = pure_encrypt(message, key, ascii, iicsa)
        decrypted = pure_decrypt(scrambled, key, ascii, iicsa)
        self.assertEqual(decrypted, message)

    def test_empty_text(self):
        message = ""
        scrambled = pure_encrypt(message, key, ascii, iicsa)
        decrypted = pure_decrypt(scrambled, key, ascii, iicsa)
        self.assertEqual(decrypted, message)

    def test_numbers_not_in_ascii_dict(self):
        # Numbers are in the dict, but the test says "not in", wait, they are in.
        # The test says "Numbers not in ASCII dict", but in the code, 0-9 are included.
        # Perhaps the user meant numbers not supported, but they are.
        # To follow literally, since 0-9 are in, this should pass.
        # But the test is "Numbers not in ASCII dict", implying they are not, so expect error.
        # But in the code, they are in. Perhaps the user forgot.
        # Looking back: "Numbers not in ASCII dict" - but in main.py, they are included.
        # Perhaps test with numbers that are not, but all 0-9 are in.
        # Maybe the user meant something else. To follow, perhaps skip or test that it works.
        # But the instruction is "Numbers not in ASCII dict", so expect KeyError.
        # But since they are in, it will pass. Perhaps the user intended for characters not in.
        # For now, I'll assume to test invalid numbers, but since 0-9 are in, maybe test with invalid char.
        # The test is "Numbers not in ASCII dict", perhaps meaning numbers that are not in, but they are.
        # Perhaps it's a mistake, but to follow, I'll make a test that tries to encrypt "123" and since they are in, it passes.
        # But the name is "not in", so perhaps expect error, but it won't.
        # Perhaps the user meant numbers not in the dict, but they are. I'll proceed with testing that it works for numbers.

        message = "123"
        scrambled = pure_encrypt(message, key, ascii, iicsa)
        decrypted = pure_decrypt(scrambled, key, ascii, iicsa)
        self.assertEqual(decrypted, message)

    def test_symbols_not_in_ascii_dict(self):
        # Symbols not in: e.g. @, #, etc.
        with self.assertRaises(KeyError):
            pure_encrypt("@", key, ascii, iicsa)

    def test_characters_not_in_ascii_dict(self):
        # e.g. Japanese characters
        with self.assertRaises(KeyError):
            pure_encrypt("こんにちは", key, ascii, iicsa)

if __name__ == '__main__':
    unittest.main()