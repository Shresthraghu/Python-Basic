# Write a program to enter 7 students data from user , store and print thier names , class , any 3 subjects marks and division in list , convert the list to tuple print all fields

# storing 7 students data in tuples . 
 
name=[]
clas=[]
phy=[]
chem=[]
math=[]
total=[]
percent=[]
division=[]

for i in range(8):
    
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

StName=tuple(name)
StClass=tuple(clas)
Stphy=tuple(phy)
Stchem=tuple(chem)
Stmath=tuple(math)
StTotal=tuple(total)
Stpercent=tuple(percent)
StDivision=tuple(division)
print("Name  Class  Physics  Chemistry  Maths  Total  Percent  Division")
for i in range(len(StName)):
    print(i,StName[i],StClass[i],Stphy[i],Stchem[i],Stmath[i],StTotal[i],Stpercent[i],StDivision[i])
