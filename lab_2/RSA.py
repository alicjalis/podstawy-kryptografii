import sympy
import random
import math


def generate_prime():
    prime = sympy.randprime(100000000, 9999999999)
    return prime



p = generate_prime()
q = generate_prime()
n = p * q
phi = (p - 1) * (q - 1)
print("phi: ", phi)

e = 2
while (e < phi):

    if (sympy.gcd(e, phi) == 1):
        break
    else:
        e = e + 1

k = 2
d = sympy.mod_inverse(e,phi)

message = "Alicja"
message = message.encode('utf-8')
message = int.from_bytes(message, byteorder='big')
c = pow(message, e, n)
print("Zaszyfrowana wiadomość: ", c)

m = pow(c, d, n)
m = m.to_bytes((m.bit_length() + 7) // 8, 'big').decode('utf-8')
print("Oryginalna wiadomość: ", m)
