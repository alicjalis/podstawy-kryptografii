import sympy
import random


def generate_prime():
    prime = sympy.randprime(1000, 9999)
    return prime


def generate_key():
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)

    e = generate_prime()
    while sympy.gcd(e, phi) != 1:
        e = generate_prime()

    d = random.randint(1000, 9999)
    while (e * d - 1) % phi != 0:
        d = random.randint(1000, 9999)

        public_key = (e, n)
        private_key = (d, n)

        return public_key, private_key


def encrypt_public(message, public_key):
    m = message
    e, n = public_key
    c = pow(m, e, n)
    return c


def decrypt_public(encrypted_message, private_key):
    c = encrypted_message
    d, n = private_key
    m = pow(c, d, n)
    return m


def encrypt_private():
    pass


public_key, private_key = generate_key()

message = 1234

encrypted_message = encrypt_public(message, public_key)
decrypted_message = decrypt_public(encrypted_message, private_key)

print("public key: ", public_key)
print("private key: ", private_key)
print("Zaszyfrowana wiadomość:", encrypted_message)
print("Odszyfrowana wiadomość:", decrypted_message)
