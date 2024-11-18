s = input() 

if (len(s) == 14) and (s[0] == "+") and (s[3]==" ") and (s[4:].isdigit()) :
    if sum(map(int,list(s[4:])))>0 :
        print("Correct")
else:
    print("Incorrect")
