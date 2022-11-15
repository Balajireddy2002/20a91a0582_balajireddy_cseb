a=input()
l=[]
flag=0
for i in a:
    if(i=="(" or i=="{" or i=="["):
        l.append(i)
    else:
        if((i==")" or i=="}" or i=="]") and len(l)==0): #starting {{{(
                flag=1
                break
        elif(i==")" and (l[-1]=="}" or l[-1]=="]")):
           flag=1
           break
        elif(i=="}" and(l[-1]=="]" or l[-1]==")")):
             flag=1
             break
        elif(i=="]" and (l[-1]=="}" or l[-1]==")")):
               flag=1
               break
        else:
            l.pop()

if((flag==1)or len(l)>=1):
    print("Invalid")
else:
    print("Valid")
    
