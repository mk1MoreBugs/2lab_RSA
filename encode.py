from calculate_mod import calculate_mod


def encode(message, e, n):
    message = int(message)
    return calculate_mod(message ** e, n)
