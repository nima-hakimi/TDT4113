"""
A person which will send (encrypt) encrypted messages
"""


from .person import Person

class Sender(Person):
  def __init__(self, cipher):
    super().__init__(cipher)

  def operate_cipher(self, message):
    return self.cipher.encode(message, self._key)

  def send(self, message, receiver):
    self.message = message
    encoded_message = self.operate_cipher(message)
    self.encoded_message = encoded_message
    receiver.receive(encoded_message)
