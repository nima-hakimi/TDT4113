"""
Unbreakable Cipher
"""


class Unbreakable:
  def __init__(self):
    self._max_signs = 95
    self._starting_sign = 32

  def generate_keys(self, key_word, no_print=False):
    encryption_key = key_word
    decryption_key = ''
    for symbol in encryption_key:
      # + _starting_sign so that mapping may start at space = 0
      sign_value = self._max_signs - ord(symbol) + self._starting_sign
      modular_value = (sign_value) % self._max_signs
      decryption_key += chr(self._starting_sign + modular_value)

    if not no_print:
      print('Encryption key:', encryption_key)
      print('Decryption key:', decryption_key)

    return encryption_key, decryption_key

  def encode(self, message, key):
    encoded_message = ""
    for i in range(len(message)):
      # - _starting_sign to make mapping start at space = 0
      key_value = ord(key[i % (len(key))]) - self._starting_sign
      modular_value = (ord(message[i]) + key_value - self._starting_sign) % self._max_signs
      encoded_symbol = chr(self._starting_sign + modular_value)
      encoded_message += encoded_symbol
    return encoded_message
  
  def decode(self, encoded_message, decryption_key):
    return self.encode(encoded_message, decryption_key)
