"""
Affine cipher - A combination of Caesar and Multiplication
"""


from .caesar import Caesar
from .multiplication import Multiplication

class Affine:
  """ Affine cipher """
  def __init__(self):
    self.caesar = Caesar()
    self.multiplication = Multiplication()

  def generate_keys(self):
    """ Generates encryption and decryption key """
    multiplication_encrypt, multiplication_decrypt = self.multiplication.generate_keys()
    caesar_encrypt, caesar_decrypt = self.caesar.generate_keys()
    encryption_key = (48, 90)  # (multiplication_encrypt, caesar_encrypt)
    decryption_key = (2, 5)  # (multiplication_decrypt, caesar_decrypt)
    return encryption_key, decryption_key

  def encode(self, message, key):
    """ Encode message with given key """
    multiplication_key = key[0]
    caesar_key = key[1]

    # Encode with Multiplication then Caesar
    partially_encoded = self.multiplication.encode(message, multiplication_key)
    encoded_message = self.caesar.encode(partially_encoded, caesar_key)
    
    return encoded_message

  def decode(self, encoded_message, decryption_keys):
    """ Decode the encoded message with the decryption key """
    multiplication_key = decryption_keys[0]
    caesar_key = decryption_keys[1]

    # Decode with Caesar then Multiplication
    partially_decoded = self.caesar.decode(encoded_message, caesar_key)
    decoded_message = self.multiplication.decode(partially_decoded, multiplication_key)
    
    return decoded_message
