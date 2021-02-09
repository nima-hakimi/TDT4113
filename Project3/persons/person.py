"""
Superclass for persons
"""


class Person:
    """ Superclass for Sender and Receiver """
    def __init__(self, cipher):
        self.cipher = cipher
        self._key = None
        self.message = ''
        self.encoded_message = ''

    """ Updates key """
    def set_key(self, key):
        self._key = key

    """ Retrieves key """
    def get_key(self):
        return self._key
