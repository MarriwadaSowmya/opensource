x,y,z = map(int,input().split())
if x <= z and x+y > z:
    print("1")
elif x+y <= z:
    print("2")
else:
    print("0")
    