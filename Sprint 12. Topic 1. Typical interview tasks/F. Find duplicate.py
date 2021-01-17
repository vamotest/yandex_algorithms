
def find_duplicate(numbers):
    
    duplicate_list = set(
        [number for number in numbers if numbers.count(number) > 1]
    )
    return duplicate_list


if __name__ == '__main__':
    n = int(input())
    list_numbers = list(map(int, input().split()))
    
    duplicate = find_duplicate(list_numbers)
    print(*duplicate)
