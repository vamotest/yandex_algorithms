# https://contest.yandex.ru/contest/18358/run-report/46293249/

def get_max_photocopy(dc_quantity, dc_capacity, count_photos=0):
    
    if dc_quantity > 1:
        dc_capacity.sort()
        
        while dc_capacity[-2] > 0:
            dc_capacity[-1] -= 1
            dc_capacity[-2] -= 1
            count_photos += 1
            dc_capacity.sort()
        return count_photos
    
    return count_photos


if __name__ == '__main__':
    n = int(input())
    array = [int(size) for size in input().split()]
    print(get_max_photocopy(n, array))
