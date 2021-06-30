s=list(map(int,input().split()))
evs=0
ods=0
for i in s:
    if(i%2==0):
        evs=evs+i
    else:
        ods=ods+i
print(evs)
print(ods)
