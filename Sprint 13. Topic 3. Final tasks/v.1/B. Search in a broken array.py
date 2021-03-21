
# https://contest.yandex.ru/contest/18358/run-report/46250021/

def find_position(array_length, desired_element, array):
    for i in range(array_length):
        if array[i] == desired_element:
            return i
    return -1


if __name__ == '__main__':
    length = int(input())
    k = int(input())
    arr = list(map(int, input().split()))
    print(find_position(length, k, arr))
