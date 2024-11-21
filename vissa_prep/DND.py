N,m = map(int,input().split())
A = list(map(int,input().split()))
num1 = 0
num2 = 0

for i in range(N):
    if A[i] % m != 0:
         num1 += A[i]
    else:
         num2 += A[i]
            
print(num2-num1)
