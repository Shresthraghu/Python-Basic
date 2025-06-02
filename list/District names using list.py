# Write a program to find any District given in a set having names of Districts . Check if the district comes in Madhya Pradesh state or not.

# District names using list :-

f=0
print("List of Districts of Madhya Pradesh")
District=["Agar Malwa","Alirajpur","Anuppur","Ashoknagar","Balaghat","Betul","Bhind","Bhopal","Burhanpur","Chhatarpur","Chhindwara","Damoh","Datia","Dewas","Dhar","Dindori","Guna","Gwalior","Harda","Indore","Jabalpur","Jhabua","Katni","Khandwa","Mahidpur","Mandla","Morena","Narsinghpur","Niwari","Panna","Pandhurna","Parase","Rehi","Rewa","Sagar","Satna","Sehore","Seoni","Shahdol","Shajapur","Sheopur","Sidhi","Singrauli","Tikamgarh","Umaria","Ujjain","Vidisha"]
for i in range(len(District)):
    print(i,District[i])
    
search=input("Enter your District name : ")
for i in District:
    if(i==search):
        
        f=1
        break
if(f==0):
    print("It does not comes in Madhya Pradesh.")
else :
    print("It  comes in Madhya Pradesh.")

