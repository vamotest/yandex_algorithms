
def bezout_recursive(a, b):
    if b == 0:
        return 1, 0, a
    y, x, g = bezout_recursive(b, a % b)
    return x, y - (a // b) * x, g


if __name__ == '__main__':
    print(*(bezout_recursive(int(input()), int(input()))))
