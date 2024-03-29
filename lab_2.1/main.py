import random

import sympy


n = sympy.randprime(1000,9999)
g = 1
while not (1 < g < n):
    g = sympy.primitive_root(n)

x = random.randint(1000,9999)
X = pow(g, x, n)

y = random.randint(1000,9999)
Y = pow(g, y, n)

ka=pow(y, x, n)
kb = pow(x, y, n)