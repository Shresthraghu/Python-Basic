#Write a program to enter record of 10 cities having city name , Temperature in Fahernheit and show the record of both Fahernheit and Celsius Temperature:-
#Record of Temparture in 10 Cities :-

cities=[]
Fah=[]
Cel=[]

for i in range(5):
    CITY=input("Enter Your City Name : ")
    cities.append(CITY)

    FAH=int(input("Enter Fahernheit Temperature"))
    Fah.append(FAH)
    
    Cels=((Fah[i]-32)*5)/9
    Cel.append(Cels)
    
print("cities  Fah  Cel")

for i in range(5):
    print(cities[i],Fah[i],Cel[i])
    
