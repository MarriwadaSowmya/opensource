N = input().strip()

sum = sum(int(digit) for digit in N)

if sum % 2 == 0:
    print("Vignesh")
else:
    print("Charan")
