#Write a Program to enter City Name, Temperature in Faherenheit and convert it into Celsius and determine the type of weather on the basis of data .

#Functions to be performed :-

#1.Create a 3 different list's of Cities Name , Faherenite Temperature , Celsius Temperature
#2.Take input of City Name and Fahernheit Temperature and  from user and add that input to the specific lists using "append Function".
#3.Now on the basis of Faherheit Temperature data convert that data to Celsius Temperature.
#4.On the Basis of Celsius data Print the appropriate message of weather condition using nested if conditions.


#Record of Temperature in 5 cities :-

cities=[]
Fah=[]
Cel=[]
weatherStatus=[]

for i in range(5):
    CITY=input("Enter Your City Name : ")
    cities.append(CITY)

    FAH=int(input("Enter Fahernheit Temperature"))
    Fah.append(FAH)
    
    Cels=((Fah[i]-32)*5)/9
    Cel.append(Cels)

for i in range(len(cities)):
    if(Cel[i]<=0 and Fah[i]<32):
        weatherStatus.append("Freezing")
    elif(Cel[i]<=10 and Fah[i]<50):
        weatherStatus.append("Very Cold")
    elif(Cel[i]<=20 and Fah[i]<70):
        weatherStatus.append("Very Cold")
    elif(Cel[i]<=30 and Fah[i]<80):
        weatherStatus.append("Normal")
    elif(Cel[i]<=40 and Fah[i]<90):
        weatherStatus.append("Hot")
    else:
        weatherStatus.append("Invalid Scale")

            
print("cities  Fah  Cel  WeatherStatus")

for i in range(5):
    print(cities[i],Fah[i],Cel[i],weatherStatus[i])
