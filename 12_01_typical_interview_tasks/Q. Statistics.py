
def main(array):
    array.sort()
    max_arr = -1
    
    for i in range(len(array)):
        left = i + 1
        right = len(array) - 1
        while right > left:
            if array[i] + array[left] + array[right] > 0:
                right -= 1
            elif array[i] + array[left] + array[right] < 0:
                left += 1
            else:
                count = array[i] * array[left] * array[right]
                if count > max_arr:
                    max_arr = count
                else:
                    right -= 1
                    left += 1
    return max_arr


if __name__ == '__main__':
    n = int(input())
    print(main(list(map(int, input().split(' ')))))
