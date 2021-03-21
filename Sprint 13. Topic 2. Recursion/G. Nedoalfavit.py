
def alphabet(letter):
    return [chr(code) for code in range(ord('a'), ord(letter) + 1)]


if __name__ == '__main__':
    print(*alphabet(str(input())))
