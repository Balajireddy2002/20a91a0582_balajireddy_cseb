number=int(input("enter the number:"))
i=1
while(i<=number):
    if(number%i==0):
        print(i)
        i=i+1
    else:
        i+=1
