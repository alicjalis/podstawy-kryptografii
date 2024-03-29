import random
import sympy

def dh_keygenerator():
    n = sympy.randprime(1000, 9999)
    g = 1
    while not (1 < g < n):
        g = sympy.primitive_root(n)

    x = random.randint(1000, 9999)
    x_pow = pow(g, x, n)

    y = random.randint(1000, 9999)
    y_pow = pow(g, y, n)

    k_a = pow(y_pow, x, n)
    k_b = pow(x_pow, y, n)

    return k_a, k_b
