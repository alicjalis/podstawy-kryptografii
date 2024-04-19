import numpy as np
from numpy.random import randint

def poly_eval(A, x):
    X = np.array([x**i for i in range(len(A))])
    y = np.sum(A*X)
    return y

def shamir_encrypt(secret, n=4, t=3):
    p = 999999999989  # Duża liczba pierwsza, większa niż sekret i liczba części

    assert p > secret, f'p > secret not satisfied ({p} <= {secret})'
    assert p > n, f'p > n not satisfied ({p} <= {n})'

    A = [secret] + list(randint(0, p, size=t-1))
    X = np.arange(n) + 1
    Y = [poly_eval(A, x) for x in X]

    # Wypisanie wyników
    print("Współczynniki wielomianu:")
    for i, x in enumerate(A):
        print(f'a_{i} = {x}')

    print("\nPunkty na krzywej:")
    for x, y in zip(X, Y):
        print(f's_{x} = f({x}) mod p = {y: 8d} mod {p} = {y % p}')

    print('\n--- ENCRYPTED ---')
    encrypted_points = ';'.join([f'{x},{y % p}' for x, y in zip(X, Y)])
    print(encrypted_points)

