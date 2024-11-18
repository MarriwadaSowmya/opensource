A = int(input())

if A not in range(1,13):
    print("Invalid")
else:
    if A in {3,4,5}:
        print("Spring")
    elif A in {6,7,8}:
        print("Summer")
    elif A in {9,10,11}:
        print("Autumn")
    else:
        print("Winter")
