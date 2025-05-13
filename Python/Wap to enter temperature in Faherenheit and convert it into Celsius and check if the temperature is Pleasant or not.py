# Write a program to enter temperature in Faherenheit and convert it into Celsius and check if the temperature is Pleasant or not .
# Pleasant temperature is between 20'C to 25'C.

fah=int(input("Enter the Fahernheit Temperature : "))
cel=((fah-32)*5)/9
print("The Celsius Temperature is :",cel)
if(cel>20 and cel<25):
    print("Temperature is Pleasant.")
else:
    print("Temperature is not Pleasant.")
