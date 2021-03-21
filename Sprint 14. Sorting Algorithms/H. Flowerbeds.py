
def find_flowerbed(data):
    data.sort()
    result = [data[0]]
    
    for index, item in enumerate(data):
        start = data[index][0]
        end = data[index][1]
        result_end = result[-1][1]
    
        if start > result_end:
            result.append(data[index])
        else:
            if end > result_end:
                result[-1][1] = end
    
    return result
    

if __name__ == '__main__':
    n = int(input())
    numbers_list = []
    for _ in range(n):
        numbers_list.append([int(number) for number in input().split()])
    
    areas = find_flowerbed(numbers_list)
    for area in areas:
        print(*area)
