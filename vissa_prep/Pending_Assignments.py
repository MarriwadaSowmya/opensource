x,y,z = map(int,input().split())
tot_minutes = z * 24 * 60
minutes = x*y
if (minutes <= tot_minutes):
    print("YES")
else:
    print("NO")
