"""
A person which will receive (decrypt) encrypted messages
"""


from .person import Person

class Receiver(Person):
  def __init__(self, cipher):
    super().__init__(cipher)

  def operate_cipher(self, encoded_message):
    return self.cipher.decode(encoded_message, self._key)

  def receive(self, encoded_message):
    self.encoded_message = encoded_message
    message = self.operate_cipher(encoded_message)
    self.message = message
