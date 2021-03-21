
# https://contest.yandex.ru/contest/18358/run-report/46293296/

def find_position(array, desired_element, left, right):

    if right >= left:
        middle = left + (right - left) // 2
    
        if array[middle] == desired_element:
            return middle
    
        if array[middle] < array[right]:
            if array[middle] < desired_element <= array[right]:
                return find_position(array, desired_element, middle + 1, right)
            return find_position(array, desired_element, left, middle - 1)
    
        if array[left] <= desired_element < array[middle]:
            return find_position(array, desired_element, left, middle - 1)
        return find_position(array, desired_element, middle + 1, right)
    
    return -1


if __name__ == '__main__':
    length = int(input())
    k = int(input())
    arr = [int(i) for i in input().split()]
    print(find_position(arr, k, left=0, right=length-1))
