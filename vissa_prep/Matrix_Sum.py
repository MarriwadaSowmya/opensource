N = int(input())
matrix = []
for i in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

result = []
for i in range(N):
    row_sum = 0
    col_sum = 0
    for j in range(N):
        row_sum += matrix[i][j]
        col_sum += matrix[j][i]
    result.append(row_sum + col_sum)

print(" ".join(map(str, result)))
