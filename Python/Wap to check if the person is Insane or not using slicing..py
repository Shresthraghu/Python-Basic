# Write a Program to check if the person is Insane or not using slicing.

MentalAge=int(input("Enter your Mental Age : "))
ActualAge=int(input("Enter your Actual Age : "))
Iq=((MentalAge*ActualAge)*100)
print("Your Iq is : ",Iq)
if(Iq>=550):
    print("You are Insane.")
else:
    print("You are not Insane.")
