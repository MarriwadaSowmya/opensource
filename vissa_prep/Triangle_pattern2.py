N = int(input())
s=1

for i in range(N):
    for j in range(i+1):
        print(s,end=" ")
    s += 1
    print()
