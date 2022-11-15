def ispar(self,a):
        flag=0
        l=[]
        for i in a:
            if(i=="(" or i=="{" or i=="["):
                l.append(i)
            else:
                if((i==")" or i=="}" or i=="]") and len(l)==0): #starting {{{(
                        flag=1
                        break
                elif(i==")" and (l[-1]=="[" or l[-1]=="{")):
                   flag=1
                   break
                elif(i=="}" and(l[-1]=="[" or l[-1]=="(")):
                     flag=1
                     break
                elif(i=="]" and (l[-1]=="{" or l[-1]=="(")):
                       flag=1
                       break
                else:
                    if(i=="}" and l[-1]=="{"):
                        l.pop()
                    if(i=="]" and l[-1]=="["):
                        l.pop()
                    if(i==")" and l[-1]=="("):
                        l.pop()
        
        if((flag==1)or len(l)>=1):
            return False
        else:
            return True
