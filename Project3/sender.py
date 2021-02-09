"""
A person which will send (encrypt) encrypted messages
"""


from person import Person

class Sender(Person):
    """ The Person to encrypt and send the message to a receiver """

    def operate_cipher(self, message):
        """ Perform encode """
        return self.cipher.encode(message, self._key)

    def send(self, message, receiver):
        """ Encode the message and send it to the receiver """
        self.message = message
        encoded_message = self.operate_cipher(message)
        self.encoded_message = encoded_message
        receiver.receive(encoded_message)
