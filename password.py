print("welcome")
username=str(input("enter user name:"))
if (username=="balajireddy"):
    password=int(input("enter password:"))
    if (password==123):
        print("password is valid")
    else:
        print("invalid password")
else:
    print("invalid user")


#output:
#testcase 1
'''enter user name:balajireddy
enter password:123
password is valid'''
#testcase 2  
'''enter user name:balajireddy
enter password:223
invalid password'''
#testcase 3
'''enter user name:reddy
invalid user'''
