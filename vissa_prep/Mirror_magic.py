N = int(input())

matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

for r in matrix:
    print(" ".join(map(str, r[::-1])))
