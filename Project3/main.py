"""
Main file to run code
"""

import sys
sys.path.insert(1, '/path/to/application/app/folder')

from persons import Sender, Receiver, Hacker
from ciphers import Caesar, Multiplication, Affine, Unbreakable, RSA


def verify_cipher(cipher_name, key_word=''):
    """ Main method to test ciphers """
    # Instantiate cipher
    cipher = None
    if cipher_name == 'caesar':
        cipher = Caesar()
    elif cipher_name == 'multiplication':
        cipher = Multiplication()
    elif cipher_name == 'affine':
        cipher = Affine()
    elif cipher_name == 'unbreakable':
        cipher = Unbreakable()
    elif cipher_name == 'rsa':
        cipher = RSA()
    else:
        raise Exception('Cipher name not recognised')

    print(('\nTesting %s cipher:\n' % cipher_name).upper())

    # Define sender and receiver
    sender = Sender(cipher)
    receiver = Receiver(cipher)

    # Distribute key(s)
    if cipher_name == 'unbreakable':
        encryption_key, decryption_key = cipher.generate_keys(key_word)
    else:
        encryption_key, decryption_key = cipher.generate_keys()
    sender.set_key(encryption_key)
    receiver.set_key(decryption_key)

    # Create message and send it
    message = "Abyssal encounter"
    # message = "aaaaaaaaaaa"
    sender.send(message, receiver)

    print("\nSender message:  ", sender.message)
    print("Sender encoded:  ", sender.encoded_message)
    print("Receiver encoded:", receiver.encoded_message)
    print("Receiver decoded:", receiver.message)

    hack = input('\nDo you want to try and hack this message? (y/n): ')
    if hack == 'y':
        hacker = Hacker(cipher)
        if cipher_name in ('caesar', 'multiplication'):
            hacker.hack_caesar_or_multiplication(sender.encoded_message)
        elif cipher_name == 'affine':
            hacker.hack_affine(sender.encoded_message)
        elif cipher_name == 'unbreakable':
            hacker.hack_unbreakable(sender.encoded_message)

CIPHER = {
    '1': 'caesar',
    '2': 'multiplication',
    '3': 'affine',
    '4': 'unbreakable',
    '5': 'rsa'
}

while True:
    print('\n')
    for key, value in zip(CIPHER.keys(), CIPHER.values()):
        print('%s: %s' % (key, value))

    CIPHER_INT = input('\nSelect cipher to verify (number): ')
    CIPHER_NAME = CIPHER[str(CIPHER_INT)]
    if CIPHER_NAME == 'unbreakable':
        KEY = input('Type key word for unbreakable cipher: ')
        verify_cipher(CIPHER_NAME, KEY)
    else:
        verify_cipher(CIPHER_NAME)

    input('\nHit Enter to start over...')
