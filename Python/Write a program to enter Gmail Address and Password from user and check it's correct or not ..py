#Write a program to enter Gmail Address and Password from user and check if the Gmail Address is "shreyraghu@gmail.com" and password is "raghu@0786"its true or not ,if its true greet the user else print appropriate message.
#solved using nested if condition's.

#Gmail Address :shreyraghu@gmail.com
#password : raghu@0786

#checking Gmail Address and password :-


GmailAdd=input("Enter your Gmail Address : ")
pas=input("Enter your password : ")
if(GmailAdd=='shreyraghu@gmail.com'):
    if(pass=='raghu@0786'):
        print("welcome back ,lets Sign in.")
    else:
        print("invalid password,try again.")
else:
    print("Gmail Address doesn't exist ,try again.")
