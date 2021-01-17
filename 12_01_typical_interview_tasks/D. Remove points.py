
def remove_zeros(li):
    new_li = [el for el in li if el != 0]
    return new_li


def main():
    c = int(input())
    li = list(map(int, input().split()))
    new_li = remove_zeros(li)
    print(*new_li)


if __name__ == '__main__':
    main()
