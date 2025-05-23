# Write a Program to store 5 students data from user and store it in a dictionary and print the all fields.

# Storing and printing Students data in Dictionary.

name=[]
clas=[]
phy=[]
chem=[]
math=[]
total=[]
percent=[]
division=[]

for i in range(3):
    
    Nm=input("Enter Student's Name : ")
    name.append(Nm)

    cl=int(input("Enter Student's Class : "))
    clas.append(cl)

    Phy=int(input("Enter Student's Physics Marks : "))
    phy.append(Phy)

    Chem=int(input("Enter Student's Chemistry Marks : "))
    chem.append(Chem)

    Math=int(input("Enter Student's Maths Marks : "))
    math.append(Math)

    Total=((Phy+Chem+Math))
    total.append(Total)

    Percent=((Total/210)*100)
    Rs=Percent
    percent.append(Rs)

    if(Percent>=60):
     division.append("first Division")
    elif(Percent<60 and Percent>=45):
     division.append("second Division")
    elif(Percent<45 and Percent>=33):
     division.append("third Division")
    else:
     division.append("failed")
    
#print("Name Physics  Chemistry  Maths  Total  Percent  Division")
#for i in range (len(name)):
    #print(i,name[i],phy[i],chem[i],math[i],total[i],percent[i],division[i])

Stu={
    "Student's Name" : name,
    "Student's class" : clas,
    "Physics Marks" : phy,
    "Chemistry Marks" : chem,
    "Maths Marks" : math,
    "Total Marks" : total,
    "Student's Percentage" : percent,
    "Division" : division
    }
for k,v in Stu.items():
    print(k,v)



