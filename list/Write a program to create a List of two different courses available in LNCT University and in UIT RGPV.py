#Write a program to create a List of two different courses available in LNCT University and in UIT RGPV . Now create a combine List and if their is any change in combine List that changes must be reflected on its copy.
#Courses List from LNCT University and UIT RGPV Bhopal.

LNCT=['Civil Engineering', 'Electronics Engineering','Bachelor of Technology', 'Electrical Engineering', 'Power Electronics', 'MBBS', 'Bachelor of Science', 'Bachelor of Business Administration', 'BCA', 'Diploma', 'Thermal Engineering', 'Master of Business Administration', 'Vlsi Design -me/m.tech', 'Chemical Engineering', 'Information Technology' ]
UITRGPV=['Perto Chemical Engineering','Automobile Engineering','Digital Communications','Structural Engineering','Heat power engineering','PharmaCeutical Chemistry','Pharmaceutics','B.Arch','Computer Science Engineering','Computer Science and Buisness System']
l1=len(LNCT)
l2=len(UITRGPV)
print("Courses offered by LNCT University :-")
for i in range(l1):
    print(i,LNCT[i])


print("Courses offered by UIT RGPV Bhopal :-")
for i in range(l2):
    print(i,UITRGPV[i])


BothCol=LNCT + UITRGPV
l3=len(BothCol)
print("After Merging Both the Lists :-")
for i in range(l3):
    print(i,BothCol[i])

#creating New List for future Upgradation :-

print("After inserting course to new list :-")
NewList=BothCol
l4=len(NewList)
BothCol.append('Humanities')
for i in range(l4):
    print(i,NewList[i])


print("By Adding position of course to new list :-")

CourseName=input("Enter New Course name you want to add : ")
Position=int(input("Enter Course Position : "))
BothCol.insert(Position,CourseName)

for i in range(l4):
    print(i,NewList[i])
