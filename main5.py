import random
from sympy import isprime, primitive_root
def generate_prime(bits=8):
    while True:
        p = random.getrandbits(bits)
        if p > 1 and isprime(p):
            return p
def diffie_hellman():
    print("=== Реализация протокола Диффи-Хелмана ===")
    print("\n1. Генерация общих параметров:")
    use_default = input("Использовать стандартные параметры? (y/n): ").lower() == 'y'

    if use_default:
        p = 23
        g = 5
        print(f"Используются стандартные параметры: p={p}, g={g}")
    else:
        p = int(input("Введите простое число p: "))
        if not isprime(p):
            print("Ошибка: p должно быть простым числом")
            return

