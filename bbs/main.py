import sympy
import random

def generate_prime(mod):
    prime = sympy.randprime(1000, 9999)
    while prime % 4 != mod:
        prime = sympy.randprime(1000, 9999)
    return prime

def are_coprime(a, b):
    return sympy.gcd(a, b) == 1

def generate_bbs_sequence(num_bits):
    p = generate_prime(3)
    q = generate_prime(3)
    N = p * q
# x i N są względnie pierwsze
    x = random.randint(2, N - 1)
    while not are_coprime(x, N):
        x = random.randint(2, N - 1)

    x0 = pow(x, 2, N)
    values = [x0]
    sequence = []

    for _ in range(num_bits):
        x_next = pow(values[-1], 2, N)
        values.append(x_next)
        if (x_next % 2 == 0):
            sequence.append('0')
        else:
            sequence.append('1')

    return ''.join(sequence)



num_bits = 20000
generated_sequence = generate_bbs_sequence(num_bits)
print("Wygenerowana sekwencja bitów:", generated_sequence)