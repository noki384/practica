from math import gcd
from sympy import mod_inverse
def generate_keys(p, q, e):
    """Генерация ключей RSA"""
    n = p * q
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)
    return (e, n), (d, n)
def encrypt(message, public_key):
    """Шифрование сообщения"""
    e, n = public_key
    if message >= n:
        raise ValueError("Сообщение должно быть меньше n")
    return pow(message, e, n)
def decrypt(ciphertext, private_key):
    """Дешифрование сообщения"""
    d, n = private_key
    return pow(ciphertext, d, n)
def main():
    print("=== Реализация RSA ===")
    try:
        # Ввод параметров
        p = int(input("Введите первое простое число p: "))
        q = int(input("Введите второе простое число q: "))

        # Выбор e
        e_input = input("Введите значение e которое должно быть взаимно простое с φ(n): ")
        e = int(e_input) if e_input else None

        # Генерация ключей
        public_key, private_key = generate_keys(p, q, e)
        print(f"\nПубличный ключ (e, n): {public_key}")
        print(f"Приватный ключ (d, n): {private_key}")

        # Работа с сообщением
        message = int(input(f"\nВведите число для шифрования (должно быть < {public_key[1]}): "))
        ciphertext = encrypt(message, public_key)
        print(f"Зашифрованное сообщение: {ciphertext}")

        decrypted = decrypt(ciphertext, private_key)
        print(f"Расшифрованное сообщение: {decrypted}")
    except ValueError as e:
        print(f"\nОшибка: {e}")
    except Exception as e:
        print(f"\nПроизошла непредвиденная ошибка: {e}")
if __name__ == "__main__":
    main()