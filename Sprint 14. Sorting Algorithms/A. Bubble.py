
# def bubble_sort(array_length, array, swapped=True):
#     while swapped:
#         swapped = False
#         for i in range(array_length - 1):
#             if array[i] > array[i + 1]:
#                 array[i], array[i + 1] = array[i + 1], array[i]
#                 swapped = True
#         print(*array)
#
#
# if __name__ == '__main__':
#     n = int(input())
#     data = [int(i) for i in input().split()]
#     print(bubble_sort(n, data))

def bubble_sort(n, data):
    flag_swapped = True
    while flag_swapped:
        flag_swapped = False
        for i in range(n - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                flag_swapped = True
    return data


n = int(input())
data = [int(i) for i in input().split(' ')]
print(*bubble_sort(n, data))
