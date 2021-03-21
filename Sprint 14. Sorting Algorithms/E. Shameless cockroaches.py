import collections


def counter(data_one, data_two):
    count = collections.Counter(data_two)
    
    answer = []
    for i in data_one:
        if count[i] > 0:
            answer.append(i)
            count[i] -= 1
    return answer


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    
    first_array = [int(element) for element in input().split()]
    second_array = [int(element) for element in input().split()]
    
    print(*counter(first_array, second_array))
