
def main():
    rows = int(input())
    columns = int(input())
    
    matrix = [list(map(int, input().split())) for _ in range(rows)]
    transport_matrix = zip(*matrix)
    
    for row in transport_matrix:
        print(*row)
    
    
if __name__ == '__main__':
    main()
