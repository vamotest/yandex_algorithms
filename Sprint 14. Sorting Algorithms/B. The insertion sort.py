
def insertion_sort(data):
    for i, element in enumerate(data):
        revers = False
        min_index = i
        
        for j in range(i, len(data)):
            if data[j] < data[min_index]:
                revers = True
                min_index = j
        
        if revers:
            data[i], data[min_index] = data[min_index], data[i]
    
    return data


if __name__ == '__main__':
    n = int(input())
    array = [int(element) for element in input().split()]
    print(*insertion_sort(array))
