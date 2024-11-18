def factorial(n):
    if n<2: 
        return 1
    return n * factorial(n-1)

x = int(input())
fact = factorial(x)
print(fact)
