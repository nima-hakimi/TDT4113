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

    def set_key(self, key):
        """ Updates key """
        self._key = key

    def get_key(self):
        """ Retrieves key """
        return self._key
