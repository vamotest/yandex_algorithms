
def quicksort(data):
    if len(data) < 2:
        return data

    pivot = data[0]
    less = [element for element in data[1:] if element <= pivot]
    greater = [element for element in data[1:] if element > pivot]
    
    return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    # n = int(input())
    array = [int(element) for element in input().split()]
    print(quicksort(array))
