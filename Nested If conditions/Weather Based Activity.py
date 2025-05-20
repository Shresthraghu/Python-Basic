# Weather Based Activity :-

# A fitness app suggests activities. If the temperature is above 30 degree Celsius and humidity is high , suggest indoor activities .If the humidity is low, recommend outdoor activities like jogging or swimming

Temp=int(input("Enter the current temperature : "))
humidity=input("Enter the current  humidity : ")

if(Temp>30):
    if(humidity=='high' or humidity=='HIGH' or humidity=='High'):
        print("You can do indoor activities like : Treadmill walking, Home execersices and play indoor games .")
    else:
        print("You can do outdoor activities like : Jogging, Swimming , Gym and play outdoor games .")        
else:
    print("You can do both  outdoor activities and indoor activities as you wish.")
    print("indoor activities like : Treadmill walking, Home execersices and play indoor games .")
    print("outdoor activities like : Jogging, Swimming , Gym and play outdoor games .") 

