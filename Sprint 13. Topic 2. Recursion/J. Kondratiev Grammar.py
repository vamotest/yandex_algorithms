

def solution(n, k):
    if n == 1:
        return 0
    if k <= 2**(n-1)/2:
        return solution(n-1, k)
    else:
        return 1 - solution(n-1, k-2**(n-1)/2)


if __name__ == '__main__':
    print(solution(int(input()), int(input())))
