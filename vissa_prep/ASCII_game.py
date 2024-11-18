s = input()
res=''
for i in s:
    if 97<=ord(i)<=122:
        res += chr(ord(i)-32)
    if 65<=ord(i)<=90:
        res += chr(ord(i)+32)
print(res)
