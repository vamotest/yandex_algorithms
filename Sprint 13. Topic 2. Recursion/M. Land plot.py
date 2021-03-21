
def get_nod(a, b):
    c = a % b
    if c == 0:
        return b
    return get_nod(b, c)


if __name__ == '__main__':
    width = int(input())
    length = int(input())

    print(get_nod(width, length))
