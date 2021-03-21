
def fibonacci(number, a=1, b=1):
    if number < 3:
        return b
    return fibonacci(number - 1, a=b, b=(a + b))


if __name__ == '__main__':
    n = int(input())
    print(fibonacci((n + 1) % 60) % 10)
