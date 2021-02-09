"""
Caesar cipher
"""


import random

class Caesar:
    def __init__(self):
        self._max_signs = 95
        self._starting_sign = 32

    def generate_keys(self):
        encryption_key = random.randint(1, 94)
        decryption_key = 95 - encryption_key

        # Print keys
        print('Encryption key:', encryption_key)
        print('Decryption key:', decryption_key)

        return encryption_key, decryption_key

    def encode(self, message, key):
        newWord = ""
        for symbol in message:
            newWord += chr(self._starting_sign + (ord(symbol) - self._starting_sign + key) % self._max_signs)
        return newWord
    
    def decode(self, encoded_mesage, decryption_key):
        return self.encode(encoded_mesage, decryption_key)
