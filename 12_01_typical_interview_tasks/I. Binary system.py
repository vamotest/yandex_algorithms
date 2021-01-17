
def sum_binary(first, second):
    return bin(int(first, 2) + int(second, 2))


if __name__ == '__main__':
    first_number = str(input())
    second_number = str(input())

    summa = sum_binary(first_number, second_number)
    print(summa)
