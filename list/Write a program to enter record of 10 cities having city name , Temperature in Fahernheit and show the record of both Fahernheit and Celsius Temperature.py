#Write a program to enter record by self of 10 cities having city name , Temperature in Fahernheit and show the record of both Fahernheit and Celsius Temperature:-
#Record of Temparture in 10 Cities by self  :-

Cels=[]
cities=['Bhopal','Indore','Ujjain','Dewas','Vidisha','Sehore','Ratlam','Gwalior','Bina','Lalitpur','Ashta']
Fah=[23,23,25,78,34,23,56,76,56,33]
l=len(cities)
for i in range(l):
    Cel=((Fah[i]-32)*5)/9
    Cels.append(Cel)
print("cities  Fah  Cels")
for i in range(l):
    print(cities[i],Fah[i],Cels[i])
    
    
