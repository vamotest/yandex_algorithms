
# https://contest.yandex.ru/contest/18970/run-report/46544727/

class Comparator:
    def __init__(self, number):
        self.number = number
        
    def __lt__(self, other):
        return self.number + other.number > other.number + self.number


def make_largest_number(numbers):
    return ''.join(sorted(numbers, key=Comparator))


if __name__ == '__main__':
    n = int(input())
    numbers_list = input().split()
    print(make_largest_number(numbers_list))
