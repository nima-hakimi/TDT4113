"""
Main file to run code
"""


from persons.sender import Sender
from persons.receiver import Receiver
from ciphers.caesar import Caesar
from ciphers.multiplication import Multiplication
from ciphers.affine import Affine
from ciphers.unbreakable import Unbreakable
from ciphers.rsa import RSA
from persons.hacker import Hacker

def verify_cipher(cipher_name, key_word=''):
    # Instanciate cipher
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
        if cipher_name == 'caesar' or cipher_name == 'multiplication':
            hacker.hack_caesar_or_multiplication(sender.encoded_message)
        elif cipher_name == 'affine':
            hacker.hack_affine(sender.encoded_message)
        elif cipher_name == 'unbreakable':
            hacker.hack_unbreakable(sender.encoded_message)

""" Code for user interface """

ciphers = {
    '1': 'caesar',
    '2': 'multiplication',
    '3': 'affine',
    '4': 'unbreakable',
    '5': 'rsa'
}

while True:
    print('\n')
    for key, value in zip(ciphers.keys(), ciphers.values()):
        print('%s: %s' % (key, value))

    cipher_int = input('\nSelect cipher to verify (number): ')
    cipher = ciphers[str(cipher_int)]
    if cipher == 'unbreakable':
        key_word = input('Type key word for unbreakable cipher: ')
        verify_cipher(cipher, key_word)
    else:
        verify_cipher(cipher)

    input('\nHit Enter to start over...')
