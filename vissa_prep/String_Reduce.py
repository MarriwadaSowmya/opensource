S = input()
count=1
for i in range(len(S)-1):
    if S[i+1]==S[i]:
        count += 1
    else:
        print(S[i],end="")
        print(count,end="")
        count = 1
        
print(S[-1],end="")
print(count)
