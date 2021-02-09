"""
Superclass for persons
"""


class Person:
  def __init__(self, cipher):
    self.cipher = cipher
    self._key = None
    self.message = ''
    self.encoded_message = ''
  
  def set_key(self, key):
    self._key = key

  def get_key(self):
    return self._key