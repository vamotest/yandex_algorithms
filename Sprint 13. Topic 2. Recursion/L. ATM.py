
def count(required_sum, coins_in_atm, value_of_coins):
    table = [0 for _ in range(required_sum + 1)]
    table[0] = 1
    
    for i in range(0, coins_in_atm):
        for j in range(value_of_coins[i], required_sum + 1):
            table[j] += table[j - value_of_coins[i]]
    return table[required_sum]


if __name__ == '__main__':
    m = int(input())
    n = int(input())
    arr = list(map(int, (input().split())))
    print(count(m, n, arr))
