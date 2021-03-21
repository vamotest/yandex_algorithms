

def get_max_perimeter(data):
    data.sort(reverse=True)
    
    for index, item in enumerate(data):
        a = data[index]
        b = data[index + 1]
        c = data[index + 2]
        
        if a < b + c:
            return a + b + c


if __name__ == '__main__':
    n = int(input())
    numbers_list = [int(number) for number in input().split()]
    print(get_max_perimeter(numbers_list))
