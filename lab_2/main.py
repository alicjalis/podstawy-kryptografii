import sympy
import random


def generate_prime():
    prime = sympy.randprime(1000, 9999)
    return prime

def generate_key():
    p = generate_prime()
    q = generate_prime()
    n = p*q
    phi = (p-1)(q-1)
    e = generate_prime()
    while sympy.gcd(e, phi) != 1:
        e = generate_prime()

    d = random.randint(100,9999)
    while (e*d-1) % phi != 0:
        d = random.randint(100,9999)
        return p,q,n,d

def encrypt_public():
    pass
