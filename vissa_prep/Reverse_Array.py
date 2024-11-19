n = int(input())
arr = list(map(int,input().split()))
res = ""
for i in range(n):
    res = str(arr[i])+" "+res
    
print(res)
