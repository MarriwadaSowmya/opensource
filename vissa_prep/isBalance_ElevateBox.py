N = int(input())
A = list(map(int,input().split()))

B = [0]*N

for i in range(N):
    Al = 0
    Ar = 0
    
    if i == 0:
        Al = 0
        for j in range(1,N):
            Ar += A[i+j]   
            
    elif i == N-1:
        Ar = 0
        for j in range(1,i+1):
            Al += A[i-j]     
            
    else:
        for j in range(1,N):
            if i+j<=N-1:
                Ar += A[i+j]
                
        for j in range(1,i+1):
            Al += A[i-j]
            
    B[i] = abs(Al - Ar)
    print(B[i],end=" ")        
            
