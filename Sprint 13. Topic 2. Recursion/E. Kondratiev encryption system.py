

def factorial(number):
    if number < 2:
        return 1
    return factorial(number - 1) * number


if __name__ == '__main__':
    n = int(input())
    print(factorial(n))
