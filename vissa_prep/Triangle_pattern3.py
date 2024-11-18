n = int(input())
space = 2 * (n-1)

for i in range(1,n+1):
  s = 1

  # numbers
  for j in range(1,i+1):
    print(s,end="")
    s+=1


  # space

  for k in range(1,space+1):
    print(" ",end="")


  # numbers
  for a in range(i,0,-1):
    print(a,end="")

  print()
  space -= 2
