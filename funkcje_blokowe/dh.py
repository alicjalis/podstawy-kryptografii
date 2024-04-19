import random
import sympy
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def padding(x):
    padding_length = AES.block_size - len(x) % AES.block_size
    return x + b'\0' * padding_length

def strip(x):
    return x.rstrip(b'\0')

def hex_rep(x):
    hex_list = []
    for b in x:
        hex_list.append(f'{b:02X}')
    return ' '.join(hex_list)

def dh_keygenerator():
    n = sympy.randprime(1000, 9999)
    g = 1
    while not (1 < g < n):
        g = sympy.primitive_root(n)

    x = random.randint(1000, 9999)
    x_pow = pow(g, x, n)

    y = random.randint(1000, 9999)
    y_pow = pow(g, y, n)

    k_a = pow(y_pow, x, n) # klucz prywatny
    k_b = pow(x_pow, y, n)

    return k_a, k_b


k_a, k_b = dh_keygenerator()

def encrypt(key, m):
    cipher = AES.new(key.to_bytes(16, byteorder='big'), AES.MODE_ECB)
    return cipher.encrypt(padding(bytes(m, 'utf-8')))

def decrypt(key, m):
    cipher = AES.new(key.to_bytes(16, byteorder='big'), AES.MODE_ECB)
    return strip(cipher.decrypt(m)).decode('utf-8')


msg = encrypt(k_a, 'Zaszyfrowana wiadomość')
print('A: encrypted =', hex_rep(msg))

rec = decrypt(k_b, msg)
print('B: decrypted =', rec)

