# Write a program to enter record of 10 city having city name Temperature in Fahernheit ,convert it into Celsius , based on Celsius Temperature also show the weather status and find out the city with Highest Temperature And lowest Temperature.

# Highest and Lowest Temperatures among 10 citites :-

cities=[]
Fah=[]
Cel=[]
weatherStatus=[]

for i in range(3):
    CITY=input("Enter Your City Name : ")
    cities.append(CITY)

    FAH=int(input("Enter Fahernheit Temperature : "))
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

for i in range(len(cities)):
    print(cities[i],Fah[i],Cel[i],weatherStatus[i])

Cel.sort(reverse=True)
HighestTemp=Cel[0]
LowestTemp=Cel[2]
HCTemp=Cel.index(HighestTemp)
LCTemp=Cel.index(LowestTemp)


print("City having Highest Celsius Temperature and its Weather Status : ",cities[LCTemp],Cel[HCTemp],"Celsisus Degrees")
print("City having Lowest Celsius Temperature and its Weather Status : ",cities[HCTemp],Cel[LCTemp],"Celsius Degrees")

Fah.sort(reverse=True)
HighestFahTemp=Fah[0]
LowestFahTemp=Fah[2]
HFT=Fah.index(HighestFahTemp)
LFT=Fah.index(LowestFahTemp)

print("City having Highest Fahernheit Temperature and its Weather Status : ",cities[LFT],Fah[HFT],"Fahernheit Degrees")
print("City having Lowest Fahernheit Temperature and its Weather Status : ",cities[HFT],Fah[LFT],"Faherenheit Degrees")
