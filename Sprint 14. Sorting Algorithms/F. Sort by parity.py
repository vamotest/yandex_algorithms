def sort_by_even(data):
    even = []
    odd = []
    for item in data:
        if item % 2 == 0:
            even.append(item)
        else:
            odd.append(item)

    result = []
    for i, item in enumerate(odd):
        result.append(even[i])
        result.append(odd[i])
    
    return result


if __name__ == '__main__':
    n = int(input())
    
    if not n:
        print('')
    else:
        array = [int(element) for element in input().split()]
        print(*sort_by_even(array))
