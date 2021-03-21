
def is_div_prizes(quantity, prizes):
    one_prize = sum(prizes) / quantity
    
    result_prize = 0
    i = 0
    while i < len(prizes):
        prize = prizes[i]
        i += 1
        if prize <= (one_prize - result_prize):
            result_prize += prize
            prizes.pop(i-1)
            i = 0
        if result_prize == one_prize:
            result_prize = 0
            quantity -= 1
    return quantity == 0


if __name__ == '__main__':
    k = int(input())
    n = int(input())
    array = [int(i) for i in input().split()]
    print(is_div_prizes(k, array))
