
# https://contest.yandex.ru/contest/18970/run-report/46595011/

def radix_sort(data):
    max_digits = len(str(max(data)))
    for i in range(max_digits):
        lists = [[] for _ in range(10)]
        for elem in data:
            sorting_digit = elem // 10**i % 10
            lists[sorting_digit].append(elem)
        data = []
        for j in range(10):
            data += lists[j]
    return data


if __name__ == '__main__':
    n = int(input())
    numbers_list = [int(element) for element in input().split()]
    print(*radix_sort(numbers_list))
