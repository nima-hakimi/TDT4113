"""
Caesar cipher
"""


import random

class Caesar:
    """ Ceasar cipher """
    def __init__(self):
        self._max_signs = 95
        self._starting_sign = 32

    def generate_keys(self):
        """ Generates encryption and decryption key """
        encryption_key = random.randint(1, 94)
        decryption_key = 95 - encryption_key

        # Print keys
        print('Encryption key:', encryption_key)
        print('Decryption key:', decryption_key)

        return encryption_key, decryption_key

    def encode(self, message, key):
        """ Encode message with given key """
        new_word = ""
        for symbol in message:
            new_word += chr(
                self._starting_sign
                + (ord(symbol) - self._starting_sign + key)
                % self._max_signs
            )
        return new_word

    def decode(self, encoded_mesage, decryption_key):
        """ Decode the encoded message with the decryption key """
        return self.encode(encoded_mesage, decryption_key)
