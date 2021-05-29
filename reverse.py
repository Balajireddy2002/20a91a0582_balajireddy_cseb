#reverse of the given number
n=int(input("enter the number"))
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("revrese of the given number is %d" %rev )


'''
expected putput

enter the number 1234
revrese of the given number is 4321
''''
