import numpy as np
from numpy.random import randint

def trivial_encrypt(secret, k, n=2):
    assert k > secret, f'k > secret not satisfied ({k} <= {secret})'
    s = secret
    keys = randint(0, k, size=n)
    s -= np.sum(keys)
    s %= k
    print('encrypted =', s)
    print('keys =', ','.join(map(str, keys)))

# Przykładowe wywołanie funkcji
trivial_encrypt(2002, 5000, 5)

def trivial_decrypt(secret, keys, k):
    s = secret
    s += sum(map(int, keys.split(',')))  # Sumowanie kluczy po konwersji na liczby całkowite
    s %= k
    print('decrypted =', s)

# Przykładowe wywołanie funkcji
trivial_decrypt(143, '217,2639,2818,785,400', 5000)
