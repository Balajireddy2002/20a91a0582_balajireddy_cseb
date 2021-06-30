s=list(map(int,input().split()))
evs=0
ods=0
for i in range(0,len(s)):
    if(i%2==0):
        evs=evs+s[i]
    else:
        ods=ods+s[i]
print(evs)
print(ods)
