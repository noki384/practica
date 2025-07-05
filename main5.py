def diffie_hellman_fully_unrestricted():
    print("=== Протокол Диффи-Хелмана===")
    p = int(input("Введите число p (любое целое, кроме 0 и 1): "))
    while p in (0, 1):
        print("Ошибка: p не может быть 0 или 1")
        p = int(input("Введите число p (любое целое, кроме 0 и 1): "))

    g = int(input("Введите число g (любое целое, кроме 0): "))
    while g == 0:
        print("Ошибка: g не может быть 0")
        g = int(input("Введите число g (любое целое, кроме 0): "))
    normalized_p = abs(p)
    if normalized_p == 1:
        normalized_p = 2
    normalized_g = g % normalized_p if normalized_p != 0 else g
    if normalized_g == 0:
        normalized_g = 1
    print("\nВведите секретные ключи (любые целые числа):")
    a = int(input("Введите секретный ключ Алисы a: "))
    b = int(input("Введите секретный ключ Боба b: "))
    try:
        A = pow(normalized_g, a, normalized_p)
        B = pow(normalized_g, b, normalized_p)
    except ValueError as e:
        print(f"Ошибка вычислений: {e}")
        return
    print("\nВычисление открытых ключей:")
    print(f"Алиса вычисляет A = {normalized_g}^{a} mod {normalized_p} = {A}")
    print(f"Боб вычисляет B = {normalized_g}^{b} mod {normalized_p} = {B}")
    print("\nОбмен ключами:")
    print(f"Алиса → Бобу: {A}")
    print(f"Боб → Алисе: {B}")
    try:
        K_alice = pow(B, a, normalized_p)
        K_bob = pow(A, b, normalized_p)
    except ValueError as e:
        print(f"Ошибка вычислений: {e}")
        return
    print("\nВычисление общего секрета:")
    print(f"Алиса вычисляет K = {B}^{a} mod {normalized_p} = {K_alice}")
    print(f"Боб вычисляет K = {A}^{b} mod {normalized_p} = {K_bob}")
    print("\nИтоговые результаты:")
    print(f"Исходные параметры: p = {p}, g = {g}")
    print(f"Фактические параметры: p = {normalized_p}, g = {normalized_g}")
    print(f"Секретные ключи: a = {a}, b = {b}")
    print(f"Открытые ключи: A = {A}, B = {B}")
    print(f"Общий секретный ключ: {K_alice}")
    if K_alice == K_bob:
        print("\nПротокол выполнен успешно! Ключи совпадают.")
    else:
        print("\nКлючи не совпали. Это возможно при некоторых значениях параметров.")
if __name__ == "__main__":
    diffie_hellman_fully_unrestricted()
