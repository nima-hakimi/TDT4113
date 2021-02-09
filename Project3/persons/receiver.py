"""
A person which will receive (decrypt) encrypted messages
"""


from person import Person

class Receiver(Person):
    """ The Person to receive encoded message and decrypt it """

    def operate_cipher(self, encoded_message):
        """ Perform decode """
        return self.cipher.decode(encoded_message, self._key)

    def receive(self, encoded_message):
        """ Decode encoded message from sender """
        self.encoded_message = encoded_message
        message = self.operate_cipher(encoded_message)
        self.message = message
