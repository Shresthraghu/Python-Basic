#Write a program to enter Vehicle Number and check if the Vehicle belongs to Bhopal or not.
#criteria for specially checking vehicle is of Bhopal or not:-

sn=input("Enter your vehicles registration number :")
rn=sn[0:4] 
if(rn=='mp04'):
    print("The vehicle belongs to Bhopal city")
else:
    print("The vehicle belongs is not belongs to Bhopal city")
