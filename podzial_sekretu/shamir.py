from numpy.random import randint
import numpy as np
def map(xs, f):
    return [f(x) for x in xs]

def join(xs, sep):
    return sep.join(xs)
from fractions import Fraction


def mod(a, b):
    return a - b * (a // b)

p = 8191


def poly_eval(A, x):
    X = np.array([x ** i for i in range(len(A))])
    y = np.sum(A * X)
    return y

# n - całkowita liczba udziałów
# t - wymagana liczba udziałów
def shamir_encrypt(secret, n=4, t=3):
    assert p > secret, f'p > secret not satisfied ({p} <= {secret})'
    assert p > n, f'p > n not satisfied ({p} <= {n})'
    A = [secret] + list(randint(0, p, size=t - 1))
    X = np.arange(n) + 1
    Y = [poly_eval(A, x) for x in X]
    print('SZYFROWANIE\n')
    print("Współczynniki wielomianu:")
    for i, x in enumerate(A): print(f'a_{i} = {x}')
    print("\nPary (x,y) reprezentujące punkt na krzywej wielomianowej: ")
    for x, y in zip(X, Y): print(f's_{x} = f({x}) mod p = {y: 8d} mod {p} = {y % p}')
    print('Wynik szyfrowania')

    print(join([f'{x},{y % p}' for x, y in zip(X, Y)], ';'))


def lagr_interp(X):
    num, den = np.ones_like(X), np.ones_like(X)
    for i, xi in enumerate(X):
        for j, xj in enumerate(X):
            if i == j: continue
            num[i] *= xj
            den[i] *= xj - xi
    return [Fraction(a, b) for a, b in zip(num, den)]


def shamir_decrypt(keys):
    X, Y = np.array([map(x.split(','), int) for x in keys.split(';')]).T
    L = lagr_interp(X)
    S = np.sum(Y * L) % p  # modulo is distributive

    print("\nDESZYFROWANIE")
    print("Mnożenie y_i (udziałów) przez wielomian Lagrange'a")
    for i in range(len(X)): print(f'y_{i}*l_{i} = {Y[i]: 6d} * {L[i]} = {Y[i] * L[i]}')
    print('Wynik deszyfrowania')
    print(S)


shamir_encrypt(1234, 6, 4)
shamir_decrypt("1,2403;2,7414;3,8074;4,4381;5,4524;6,310")