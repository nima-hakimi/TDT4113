"""
Multiplication cipher
This cipher multiplies the key with (ord(letter) - 32),
meaning it is 0-indexed, starting at space.
"""


import random
import math
from crypto_utils import modular_inverse

class Multiplication:
    """ Multiplication cipher """
    def __init__(self):
        self._max_signs = 95
        self._starting_sign = 32

    def generate_keys(self):
        """ Generates encryption and decryption key """
        encryption_key = None

        # Generate a random encryption key:
        while True:
            candidate = random.randint(2, self._max_signs)
            if math.gcd(candidate, self._max_signs) == 1:
                encryption_key = candidate
                break
        
        # Find the decryption key for the given encryption key
        decryption_key = modular_inverse(encryption_key, self._max_signs)

        # Printing for verification of keys:
        print("Encryption key: " + str(encryption_key))
        print("Decryption key: " + str(decryption_key))
        mod_value = encryption_key * decryption_key % self._max_signs
        print("Verify inversion: %s * %s mod %s = %s " %
            (encryption_key, decryption_key, self._max_signs, mod_value))

        return encryption_key, decryption_key

    def encode(self, message, key):
        """ Encode message with given key """
        new_word = ""
        for symbol in message:
            #print('key:', key)
            #print(self._starting_sign + ((ord(symbol) - self._starting_sign) * key))
            new_word += chr(self._starting_sign + ((ord(symbol) - self._starting_sign) * key) % self._max_signs)
        return new_word
    
    def decode(self, encoded_message, decryption_key):
        """ Decode the encoded message with the decryption key """
        return self.encode(encoded_message, decryption_key)