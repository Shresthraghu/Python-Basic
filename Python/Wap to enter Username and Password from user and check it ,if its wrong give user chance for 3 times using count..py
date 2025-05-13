# Write a program to enter Username and Password from user and check , if it's wrong give user chances for 3 times using count.

c=0
while(True):
    UserName=input("Enter User Name : ")
    Password=input("Enter Password : ")
    if(UserName=='shrey'):
        if(Password=='shrey_123'):
            print("Welcome Back shrey :)")
        else:
            print("Invalid Password ,try again.")
    else:
        print("Invalid User Name ,try again.")
    ans=input("Do you want to try again?")
    if(ans!='y'):
        break
    c=c+1
    if(c>=3):
        print("You have reached maximum limit of trying , come again later.")
        break
       
        
                
        
        
