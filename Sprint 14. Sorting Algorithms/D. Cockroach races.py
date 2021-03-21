
def check_cheaters(data_one, data_two):
    intersection = set(data_one) & set(data_two)
    
    data = []
    for element in data_one:
        if element in intersection and element not in data:
            data.append(element)
    return data


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    
    if n < 1 or m < 1:
        print('')
    else:
        first_array = [int(element) for element in input().split()]
        second_array = [int(element) for element in input().split()]
        
        print(*check_cheaters(first_array, second_array))
