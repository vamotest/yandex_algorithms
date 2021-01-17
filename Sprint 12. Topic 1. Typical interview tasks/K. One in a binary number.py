
def binary_convert(number):
    binary_number = ''
    while number > 0:
        binary_number = str(number % 2) + binary_number
        number = number // 2
    return binary_number


def find_amount(binary_number):
    return binary_number.count('1')
    

if __name__ == '__main__':
    count = find_amount(binary_convert(int(input())))
    print(count)
