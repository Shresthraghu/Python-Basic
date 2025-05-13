#Wap to enter 5 students data from user ,store and print their name,
#class,any 3 subjects marks, calculate total marks andprint all fields
#using list and Append variable.


#Student Data:-


#Wap to enter 5 students data from user ,store and print their name,
#class,any 3 subjects marks, calculate total marks andprint all fields
#using list and Append variable.


#Student Data:-

nm=[]
cls=[]
phy=[]
chem=[]
math=[]
total=[]
for i in range(5):
    name=input("Enter Student's Name :- ")
    nm.append(name)
    standard=input("Enter Student's Class :- ")
    cls.append(standard)
    physics=int(input("Enter Students's Marks in Physics subject :- "))
    phy.append(physics)
    chemistry=int(input("Enter Students's Marks in Chemistry subject :- "))
    chem.append(chemistry)
    mathematics=int(input("Enter Students's Marks in Maths subject :- "))
    math.append(mathematics)
    totalMarks=phy+chem+math
    total.append(totalMarks)

print(nm)
print(cls)
print(phy)
print(chem)
print(math)
print(total)
for i in range(5):
    print(i,nm[i],cls[i],phy[i],chem[i],math[i],total[i])
