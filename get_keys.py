def get_keys(p, q):
    n = p * q
    fi = (p - 1) * (q - 1)

    while True:
        e = input_e(fi)
        if check_prime_number_e(e, fi):
            break

    d = calculate_number_d(fi, e)
    if d[1] > d[2]:
        d = d[1]
    else:
        d = d[2]

    return {
        "n": n,
        "e": e,
        "d": d,
    }


def input_e(fi):
    return int(input(f"Введите число e от 1 до {fi}, взаимно простое со значением {fi}: "))


def check_prime_number_e(e, fi):
    is_prime_number = True
    for i in range(2, fi):
        if fi % i == 0 and e % i == 0:
            print(f"Число не взаимно простое со значением {fi}!")
            is_prime_number = False
            break
    return True if is_prime_number else False


def calculate_number_d(a, b):
    if b == 0:
        return a, 1, 0

    else:
        d, x, y = calculate_number_d(b, a % b)
        return d, y, x - y * (a // b)
