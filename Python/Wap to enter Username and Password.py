#Write a program to enter username and pass check if the username is "prema" and password
#is "p123" then greet the user ,else print appropriate message.
#checking user name and password
user=input("Enter your user name : ")
pas=input("Enter your password : ")
if(user=='prema'):
    if(pas=='p123'):
        print("welcome back")
    else:
        print("invalid password,try again.")
else:
    print("User name doesn't exist ,try again.")

