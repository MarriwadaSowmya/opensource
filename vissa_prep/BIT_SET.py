N = int(input())
i = int(input())
k = 1 << (i-1)

if N & k:
    print("true")
else:
    print("false")
