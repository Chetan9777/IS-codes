# -*- coding: utf-8 -*-
"""RSA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZLEVpHbiI-XKa-Q2SkrwKLvf0_WqE2LC
"""

import random

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to find the greatest common divisor (GCD)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to generate keys (public and private)
def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal.")

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # Use Extended Euclidean Algorithm to generate the private key
    d = pow(e, -1, phi)

    # Return public and private keypair
    # Public key: (e, n)
    # Private key: (d, n)
    return ((e, n), (d, n))

# Function to encrypt plaintext using public key
def encrypt(public_key, plaintext, base=10):
    e, n = public_key
    if base == 2:
        plaintext = int(plaintext, 2)
    # Apply the public key formula: ciphertext = plaintext^e mod n
    encrypted_msg = pow(plaintext, e, n)
    return encrypted_msg

# Function to decrypt ciphertext using private key
def decrypt(private_key, ciphertext, base=10):
    d, n = private_key
    # Apply the private key formula: plaintext = ciphertext^d mod n
    decrypted_msg = pow(ciphertext, d, n)
    if base == 2:
        decrypted_msg = bin(decrypted_msg)[2:]
    return decrypted_msg

# Main program
if __name__ == '__main__':
    # Choose two prime numbers
    p = int(input("Enter a prime number (p): "))
    q = int(input("Enter another prime number (q): "))
    # Generate public and private keys
    public_key, private_key = generate_keypair(p, q)
    print("Public Key (e, n):", public_key)
    print("Private Key (d, n):", private_key)

    # Get user input for message and base
    message = input("Enter the message: ")
    base = int(input("Enter the base (10 for decimal, 2 for binary): "))

    # Encrypt the message
    if base == 2:
        plaintext = int(message, 2)
    else:
        plaintext = int(message)
    encrypted_message = encrypt(public_key, plaintext)
    print("Encrypted Message:", encrypted_message)

    # Decrypt the encrypted message
    decrypted_message = decrypt(private_key, encrypted_message, base)
    print("Decrypted Message:", decrypted_message)