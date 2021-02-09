""" RSA """


import random
from crypto_utils import generate_random_prime, modular_inverse, blocks_from_text, text_from_blocks


class RSA:
    """ RSA """
    def generate_keys(self):
        """ Generates encryption and decryption key """
        # Number of bits needed to represent ASCII
        num_of_bits = 8

        # Make random primes until they are not equal
        prime1 = generate_random_prime(num_of_bits)
        prime2 = generate_random_prime(num_of_bits)
        while prime1 == prime2:
            prime1 = generate_random_prime(num_of_bits)
            prime2 = generate_random_prime(num_of_bits)

        prime_product = prime1 * prime2
        phi = (prime1 - 1) * (prime2 - 1)

        rand_num = random.randint(3, phi - 1)

        inverse_rand_num = modular_inverse(rand_num, phi)

        # Have not found an inverse:
        while not inverse_rand_num:
            rand_num = random.randint(3, phi - 1)
            inverse_rand_num = modular_inverse(rand_num, phi)

        public_key = (prime_product, rand_num)
        secret_key = (prime_product, inverse_rand_num)
        
        print('Valid key pair found!')
        print('Public key:', public_key)
        print('Secret key:', secret_key)

        return secret_key, public_key

    def encode(self, message, public_key):
        """ Encode message with given key """
        blocks = blocks_from_text(message, 2)

        encoded_message = []

        sum_primes = public_key[0]
        rand_num = public_key[1]

        for number in blocks:
            temp = pow(number, rand_num, sum_primes)
            encoded_message.append(temp)

        return encoded_message

    def decode(self, blocks, secret_key):
        """ Decode the encoded message with the decryption key """
        decoded_numbers = []

        sum_primes = secret_key[0]
        inverse_rand_num = secret_key[1]

        for number in blocks:
            decoded_number = pow(number, inverse_rand_num, sum_primes)
            decoded_numbers.append(decoded_number)

        decoded_message = text_from_blocks(decoded_numbers, 8)

        return decoded_message
