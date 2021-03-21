import collections


def count_sorting(data):
    count = collections.Counter(data)
    result = '0 ' * count.get(0) + '1 ' * count.get(1) + '2 ' * count.get(2)
    return result.split()


if __name__ == '__main__':
    n = int(input())
    
    if not n:
        print()
    else:
        numbers_list = [int(number) for number in input().split()]
        print(*count_sorting(numbers_list))
