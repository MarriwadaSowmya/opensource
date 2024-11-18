N = int(input())
num = 1

for i in range(1, N + 1):
    row = []
    for j in range(i):
        row.append(str(num))
        num += 1
    print(" ".join(row))
