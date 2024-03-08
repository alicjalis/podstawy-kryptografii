import sympy  # funkcja do zwracania liczb pierwszych
import random


def generate_prime(mod):
    prime = sympy.randprime(1000, 9999)  # 4 cyfrowe liczby
    while prime % 4 != mod:
        prime = sympy.randprime(1000, 9999)
    return prime


def are_coprime(a, b):
    return sympy.gcd(a, b) == 1

#ctr alt l zeby formatowac
p = generate_prime(3)
q = generate_prime(3)

print("p =", p)
print("q =", q)

N = p * q
print("Iloczyn p i q =", N)

x = random.randint(2, N - 1)
while not are_coprime(x, N):
    x = random.randint(2, N - 1)

print("Wylosowana liczba x:", x)

x0 = pow(x, 2, N)
# x^2 % N
print("Wartość pierwotna generatora:", x0)

values = [x] # czy tu x0??
num_bits = 20000

for _ in range (num_bits):
    xi = pow(values[-1], 2, N)
    # values[-1]^2 % N
    values.append(xi)

# konwersja na łańcuch bitów
binary_string =binary_string = ''.join(['1' if bit % 2 == 1 else '0' for bit in values])

# wyświetlenie pierwszych 100
print(binary_string[:100])

#parametryzować wszystko co się da
