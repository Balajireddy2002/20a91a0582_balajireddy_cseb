a=int(input("enter number"))
b=int(input("enter exponent"))
c=pow(a,b)
r=c%10
print("%d^%d=%d"%(a,b,c))
print("last digit of %d is %d"%(c,r))
#expected out put:
"""enter number5
enter exponent2
last digit of 25 is 5"""
