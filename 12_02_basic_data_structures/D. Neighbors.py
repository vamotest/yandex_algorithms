
def main(columns, matrix, x, y):
    answer = []
    
    a = x
    b = y + 1
    if b < columns:
        answer.append(int(matrix[a][b]))

    a = x - 1
    b = y
    if a > -1:
        answer.append(int(matrix[a][b]))

    a = x
    b = y - 1
    if b > -1:
        answer.append(int(matrix[a][b]))

    a = x + 1
    b = y
    if a < rows:
        answer.append(int(matrix[a][b]))

    answer.sort()
    return answer
    
    
if __name__ == '__main__':
    rows = int(input())
    columns = int(input())
    
    matrix = [input().split() for _ in range(rows)]
    print(*main(columns, matrix, int(input()), int(input())))
