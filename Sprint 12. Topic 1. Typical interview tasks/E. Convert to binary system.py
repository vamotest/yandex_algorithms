
def binary_convert(number):
    binary_number = ''
    while number > 0:
        binary_number = str(number % 2) + binary_number
        number = number // 2
    return binary_number


if __name__ == '__main__':
    binary = binary_convert(int(input()))
    print(binary)
