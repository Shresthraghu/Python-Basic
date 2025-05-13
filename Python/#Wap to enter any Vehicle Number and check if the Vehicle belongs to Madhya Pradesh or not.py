#Write a program to enter any Vehicle Number and check if the Vehicle belongs to Madhya Pradesh or not :-
#checking registration number in MP :-

vehNo=input("Enter vehicle Number : ")
a=vehNo[:2]
b=vehNo[2:4]
if(a=='mp'):
   print("The vehicle belongs to MP state.")
   if(b=='04'):
       print("The vehicle belongs to Bhopal district.")
   elif(b=='08'):
       print("The vehicle belongs to Guna district.")
   elif(b=='09'):
       print("The vehicle belongs to Indore district.")
   elif(b=='13'):
       print("The vehicle belongs to Dewas district.")
   elif(b=='41'):
       print("The vehicle belongs to Ujjain district.")
   else:
       print("vehicle is of Mp sate but district is not known")
else:
    print("The vehicle does not belongs to MP state.")
