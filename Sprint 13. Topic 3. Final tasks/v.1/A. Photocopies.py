# https://contest.yandex.ru/contest/18358/run-report/46248741/

def get_max_photocopy(size_dc):
    max_capacity = max(size_dc)
    amount = sum(size_dc)
    
    half_amount = amount // 2
    if half_amount < max_capacity:
        return amount - max_capacity
    return half_amount


if __name__ == '__main__':
    quantity_dc = int(input())
    arr = list(map(int, input().split()))
    print(get_max_photocopy(arr))
