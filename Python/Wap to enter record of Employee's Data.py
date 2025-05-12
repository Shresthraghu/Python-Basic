# Wap to enter record of an employee having employee name, code , dept, and salary checck if the employee is having salary in less than 4 digits then do not do anything if the employee having salary in 5 digits then allow him 10% HRA if the salary is in 6 digits then allow him 30% HRA ,else allow him 50 % HRA find out total amount of salary and print all fields :-

#Employee Data :-
employName=input("Enter Employee's Name :")
employCode=int(input("Enter Employee's Code :"))
employDept=input("Enter Employee's Department :")
employDesign=input("Enter Employee's Designation :")
employSalary=input("Enter Employee's Salary : ")
ds=len(employSalary)
employSalary=int(employSalary)
if(ds<4):
    hra=0
    
elif(ds<5):
    hra=((employSalary*10)/100)
elif(ds<6):
    hra=((employSalary*30)/100)
else:
    hra=((employSalary*50)/100)
print("Employee's Name : ",employName)
print("Employee's Code : ",employCode)
print("Employee's Department : ",employDept)
print("Employee's Designation : ",employDesign)
print("Employee's Salary : ",employSalary)
totalSalary=(employSalary+hra)
print("Employee HRA",hra)
print("Employee's Total Salary : ",totalSalary)
