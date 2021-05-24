n=int(input("enter money"))
print("total bill is:",n)
if(n>1000 and n<=2000):
   c=(n*10)/100
elif(n>2000 and n<=5000):
    c=(n*20)/100
elif(n>3000 and n<=5000):
    c=(n*30)/100
elif(n>5000):
   c=(n*40)/100
else:
    print("total bill is",n)
print("discount is :",c)
print("net amount is :",n-c)
 #expected out put 
"""enter money2600
total bill is: 2600
discount is : 520.0
net amount is : 2080.0"""
# out put 
"""enter money2600
total bill is: 2600
discount is : 520.0
net amount is : 2080.0"""
