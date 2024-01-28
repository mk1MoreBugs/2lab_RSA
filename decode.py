from calculate_mod import calculate_mod


def decode(crypt, d, n):
    return calculate_mod(int(crypt) ** d, n)
