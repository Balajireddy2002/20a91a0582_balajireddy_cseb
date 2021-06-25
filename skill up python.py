                                                 #BALAJI REDDY
                    #TECHINICAL HUB
                    #SKILL UP PYTHON


#prime number programs
"""n=int(input("enter number"))
i=2
s=1
for i in range(i,n,s):
    if(n%i==0):                      #one method
        print(n,"not primr")
        break
    else:
        print(n,"primr number")"""
#another method
"""n=int(input("enter number"))
i=1
s=1
count=0
for i in range(i,(n//2)+1,s):
    if(n%i==0):                      #one method
       count=count+1
if(count==1):
    print(n,"prime number")
else:
    print(n,"not prime")"""
#sqrt method
"""n=int(input("enter nimber"))
i=1
count=0
import math   #FOR INTRODUCING SQUARE ROOT    this is a header file
s=int(math.sqrt(n))
for i in range(i,s,1):
    if(s%i==0):                      #one method
       count=count+1
if(count==0):
    print(n,"prime")
else:
    print(n,"not prime")"""
# _0_
 #reverse number
"""n=int(input("enter a number"))
sum=0
temp=n
while(n>0):
    r=n%10
    sum=sum*10+r
    n=n//10
print(sum)"""
#palindrome number
"""n=int(input("enter a number"))
sum=0
temp=n
while(temp!=0):
    r=temp%10
    sum=sum*10+r
    temp=temp//10
if(sum==n):
    print(n,"palindrome number")
else:
    print(n,"not palindrome")"""
#perfect number
"""n=int(input("enter a number"))
sum=0
temp=n                           #not completed perfect
while(temp!=0):
    r=temp%10
    sum=sum*10+r
    temp=temp//10"""
#armstrong number
"""n=int(input("enter a number"))
sum=0
temp=n
while(temp>0):
    r=temp%10
    c=r**3
    sum=sum+c
    temp=temp//10
if(sum==n):
    print(n,"armstrong number")
else:
    print(n,"not armstrong ")"""
#reverse or palindrome simple logic
'''n=input("enter the number")
if (n==n[::-1]):     #supported for strings
    print("armsrong number")
else:
    print("not armstrong number")'''
#fabinocci series:sum of before two trms
"""n=int(input("enter no of terms in the series:"))
a=0
b=1
print(a)
print(b)
for i in range(3,n+1):
      c=a+b
      a=b
      b=c
      print(b)"""

#tribinocci series:sum of before three trms
"""n=int(input("enter no of terms in the series:"))
a=0
b=1
c=1
print(a)
print(b)
print(c)
for i in range(4,n+1):
      d=a+b+c
      a=b
      b=c
      c=d
      print(c)"""

# Jacobsthal sequence is an additive sequence similar to the Fibonacci sequence,
#defined by the recurrence relation Jn = Jn-1 + 2Jn-2, with initial terms J0 = 0 and J1 = 1.
#A number in the sequence is called a Jacobsthal number.
"""program......
.............."""
#jacobstal series
"""n=int(input("enter no of terms in the series:"))
a=0
b=1
print(a)
print(b)
for i in range(3,n+1):
      c=b+2*a
      a=b
      b=c
      print(b)"""
#lcm of two numbers #by me
"""a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))             
i=b
n=a*b
while(i<=n+1):
      if(i%a==0 and i%b==0):
            print("lcm of %d,%d is %d"%(a,b,i))
            break
      else:
           i=i+1"""
#lcm of two numbers
"""a=int(input())
b=int(input())
c=b
while True:#this is infinate loop
      if(c%a==0 and c%b==0):
             print("lcm of %d,%d is %d"%(a,b,c))
             break
      c=c+1"""
#GCD of two numbers
"""a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))             
i=b
if(b>a):
    a,b=b,a
for i in range(b,0,-1):
    if(a%i==0 and b%i==0):
        print(i)
        break
    i=i+1"""
#arthematic progression:
"""n=int(input("enter no of terms in the series:"))
a=int(input("enter initial value:"))
d=int(input("enter common differnce:"))
print(a)
for i in range(1,n):
    b=a+i*d
    print(b)"""
#geomertic progression
"""n=int(input("enter no of terms in the series:"))
a=int(input("enter initial value:"))
r=int(input("enter common ratio:"))
print(a)
for i in range(1,n):
    b=a*r**i
    print(b)"""
#10/6/21
#functions:
"""def example(a,b):#formal parameters    #we can use any other variables #these are only for name sake
    print(a+b)
a=int(input("enter number"))
b=int(input("enter number"))
example(a,b)#actual parameters"""
#NOTE
#no of actual parameters==no of formal parameters(other wise it will leads to type error)
"""def example(a,b):#formal parameters    #we can use any other variables #these are only for name sake
   return a+b
a=int(input("enter number"))
b=int(input("enter number"))
c=example(a,b)
print(c)"""#actual parameters"""
####prime number by functions 
"""def prime(i,n,count):
    prime=True
    notprime=False
    for i in range(i,(n//2)+1):
        if(n%i==0):
            count=count+1
    if(count==1):
        return prime
    else:
        return notprime
n=int(input("enter number"))
i=1
count=0
c=prime(i,n,count)
print(c)"""
####tribinicco series using functions
"""def tri(n):
    a=0
    b=1
    c=1
    print(a)
    print(b)
    print(c)
    for i in range(4,n+1):
        d=a+b+c
        a=b
        b=c
        c=d
        print(c)
n=int(input("enter no of terms in the series"))
tri(n)"""
###ARTHEMATIC OPERATIONS using functions
"""def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
a=int(input("enter a nmber"))
b=int(input("enter a nmber"))
c=add(a,b)
print(c)
c=sub(a,b)
print(c)
c=multi(a,b)
print(c)"""
#example of functions
"""def example():
    a=12
    print(a)
a=10
print(a)
example()#here the output is 12 since we called function
print(a)"""#here a=10
# remember that the scope of a variable is with in ina function.
#the variable which declared outside the function is called global variable.it is having global scope
#the variable which declared inside the function is called local variable.it is having local scope
######------------------------------------###
"""def example():
    print(a)
global a  # by using this keyword we can declare globally
a=10
print(a)
example()
print(a)"""
##---------------------------------------###
"""def example():
    global a
    a=12
    print(a)#12
a=10
print(a)#10
example()# 12 
print(a)#12"""
#----------------#
#prime number programs
"""def prime(n):
    for i in range(2,n):
       if(n%i==0):          #return terminates the loop when the condition satisfied simply it acts as braek
           return False
    else:
        return True
def prime2(n):
    for i in range(2,n):
       if(n%i==0):          #return terminates the loop when the condition satisfied simply it acts as braek
           print('not prime')
           break
       else:
        print('prime number')      
a=int(input("enter number"))
p=int(input("enter number"))
print(prime(a))
print(prime2(p))"""
#-----------------------------------------#
#factorial number
"""n=int(input('enter a number'))
f=1
for i in range(1,n+1):
    f=f*i
print("factoraial of %d is %d"%(n,f))"""
#by functions
#factorial number
"""def fact(n):
    f=1
    for i in range(1,n+1):
       f=f*i
    return f
n=int(input('enter a number'))
print(fact(n))"""
#facrorial by recursion
"""def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return(n*fact(n-1))
n=int(input('enter a number'))
print(fact(n))"""
#-------------------------#
#lcm of a number by recursion
"""def lcm(c,a,b):
      if(c%a==0 and c%b==0):
             return c
      else:
            c=c+1
            return(lcm(c,a,b))
a=int(input('enter a number'))
b=int(input('enter a number'))
c=b
print(lcm(c,a,b))"""
#------------------------#
#lenght of the string by using recursion
"""def str(a):
      if a is '':
            return 0
      else:
            return(1+str([1: ]))
b=input('enter a string')
print(str(b))"""
#---------------------------#
#immediate prime number
"""def prime(n):
    for i in range(2,n):
       if(n%i==0):          #return terminates the loop when the condition satisfied simply it acts as braek
           return False
    else:
        return True
n=int(input())
prime(n)
if prime(n):
      print(n,'prime number')
while True:
      n=n+1
      if prime(n):
            print(n,'prime number')
            break"""
#circular primes
"""def prime(n):
    for i in range(2,n):
       if(n%i==0):          
           return False
    else:
        return True
n=int(input())
prime(n)
sum=0
if prime(n):   
   temp=n
   while(temp>0):
      r=temp%10
      sum=sum*10+r
      temp=temp//10
   prime(sum)
if(prime(n) and prime(sum)):
      print(True)
else:
      print(False)"""
#--------------------------------#
"""def prime(n):
    for i in range(2,n):
       if(n%i==0):          #return terminates the loop when the condition satisfied simply it acts as braek
           return False
    else:
        return True
a=int(input('enter a number'))
print(prime(a))
temp=a
if prime(a):
    while(temp>0):
      r=temp%10
      prime(r)
      if prime(r)==False:
            print("not")
      else:
         print(r,"true")    
      temp=temp//10"""
#-----------------------------------------#
#mega prime
"""def prime(n):
    for i in range(2,n):
       if(n%i==0):          #return terminates the loop when the condition satisfied simply it acts as braek
           return False
    else:
        return True
def mp(n):
      if prime(n):
            while n:
                  r=n%10
                  if prime(r)==False:
                        return False
                  n=n//10
            else:
                  return True
      else:
            return False
n=int(input())

print(mp(n))"""
#---------------------------------------#
#PATTERN PROGRAMS
"""n=int(input())
for i in range(1,n+1):
      for j in range(1,n+1):
            print('*',end='')
      print(end='\n')"""

#input
"""n=int(input())
s=-1
for i in range(1,n+1):
      for j in range(1,i):
            print('*',end=' ')
      print(end='\n')"""
#===============================#
"""n=int(input())                                  
for i in range(1,n+1):
      for j in range(n,i-1,s):
            print('*',end=' ')
      print(end='\n')"""
#---------------------------#
#converting decimal -binary and printing last number
"""n=int(input('enter number'))
rem=0
s=''
while True:
     rem=n%2
     print(rem)
     s+=str(rem)
     n=n//2
     if(n<=1):
          print(1)
          s+=str(1)
          break
     print('4 bitof given decimal number is',s[3])"""
#------------------------------------#
n=int(input())
n=bin(n)
print(n)
n=n[2:]#to remove last two bits and the array starts from index2 and it will be zero
print(n)
n=n[::-1]
print(n)
print(n[3])






























      

      


      
