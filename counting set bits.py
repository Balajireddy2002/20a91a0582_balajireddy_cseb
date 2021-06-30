# Function to get no of set bits in binary
# representation of positive integer n */
def  countSetBits(n):
    count = 0
    while (n):#if n become 0 then the condition fails
        if(n&1==1):
            count+=1            
        n=n>>1
    return count
  
 #set bits means no of 1's in bin representation of given num 
# Program to test function countSetBits */
i = int(input())
print(countSetBits(i))
