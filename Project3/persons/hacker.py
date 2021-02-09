"""
A class to brute force crack the ciphers
"""


import os
from .receiver import Receiver

class Hacker(Receiver):
    def __init__(self, cipher):
            super().__init__(cipher)
            self.path = os.path.dirname(__file__)

    def hack_caesar_or_multiplication(self, encoded_message):
        """ Try to decode with every possible key """
        for key in range(1, 95):
            decoded_message = self.cipher.decode(encoded_message, key)
            encoded_message_list = decoded_message.lower().split() 
            counter = 0
            try:
                with open(self.path + "/english_words.txt", "r") as file:
                    for english_word in file.readlines():
                        english_word = english_word.strip()
                        if english_word in encoded_message_list: counter += 1
                        if counter == len(encoded_message_list):
                            print('\n( ͡° ͜ʖ ͡°) YOU HAVE BEEN HACKED ( ͡° ͜ʖ ͡°)')
                            print('The hacker found a key:', key)
                            print('The original message is:', decoded_message)
                            return
            except FileNotFoundError:
                raise Exception('Filen finnes ikke')
        print('The hacker found nothing :(')


    def hack_affine(self, encoded_message):
        """ Try to decode with every possible key pair """
        for i in range(1, 95):
            for j in range(1, 95):
                key = (i, j)
                print('Trying key:', key)
                decoded_message = self.cipher.decode(encoded_message, key)
                encoded_message_list = decoded_message.lower().split() 
                counter = 0
                try:
                    with open(self.path + "/english_words.txt", "r") as file:
                        for english_word in file.readlines():
                            english_word = english_word.strip()
                            if english_word in encoded_message_list:
                                counter += 1
                            if counter == len(encoded_message_list):
                                print('\n( ͡° ͜ʖ ͡°) YOU HAVE BEEN HACKED ( ͡° ͜ʖ ͡°)')
                                print('The hacker found a key:', key)
                                print('The original message is:', decoded_message)
                                return
                except FileNotFoundError:
                    print('Filen finnes ikke')
        print('The hacker found nothing :(')

    def hack_unbreakable(self, encoded_message):
        """
        Hack the "unbreakable" cipher:
        make a list of every word and try
        every word as key
        """
        words = []
        try:
            with open(self.path + "/english_words.txt", "r") as file:
                for english_word in file.readlines():
                    english_word = english_word.strip()
                    words.append(english_word)
        except FileNotFoundError:
            print("File not found")

        counter = 0
        for word in words:
            key_pair = self.cipher.generate_keys(word, no_print=True)
            decryption_key = key_pair[1]
            print('Trying key:', word)
            decoded_message = self.cipher.decode(encoded_message, decryption_key)
            encoded_message_list = decoded_message.split()

            for l in words:
                if l in encoded_message_list:
                    counter += 1
            if counter == len(encoded_message_list):
                print('\n( ͡° ͜ʖ ͡°) YOU HAVE BEEN HACKED ( ͡° ͜ʖ ͡°)')
                print('The hacker found a key:', word)
                print('The original message is:', decoded_message)
                return
        print('The hacker found nothing :(')
