from decode import decode
from encode import encode
from get_keys import get_keys


if __name__ == '__main__':
    p, q = tuple(map(int, input("Введите числа p и q: ").split()))
    keys = get_keys(p, q)
    print(keys)

    choice = int(input("Выберите: 1 - Зашифровать сообщение, 2 - Расшифровать \n"))
    if choice == 1:
        message = input("Введите сообщение: ")
        crypt = encode(message, keys["e"], keys["n"])
        print(crypt)

    elif choice == 2:
        crypt = input("Введите зашифрованное сообщение: ")
        message = decode(crypt, keys["d"], keys["n"])
        print(message)
