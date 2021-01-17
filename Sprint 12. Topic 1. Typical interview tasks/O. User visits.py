
def unique(first, second):
    return sorted(first + second)
    
    
if __name__ == '__main__':
    serv1 = [x for x in list(map(int, input().split())) if x != 0]
    n = int(input())
    m = int(input())
    serv2 = [x for x in list(map(int, input().split()))]
    
    result = unique(serv1, serv2)
    print(*result)
