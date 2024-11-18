x,n = map(int,input().split())
a = x * 100
b = n - a
if b <= 0:
    print("0")
else:
    print((b+99) // 100) #ceil

# floor of a/b = a//b
# ceil of a/b  = (a + (b-1)) // b 

