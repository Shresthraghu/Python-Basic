# Write a program to enter Record of an Employee having Employee Name , Employee Department , Employee Salary and find out the person with Highest Salary and Lowest Salary  and print all the fields.


# Task performed in this code :-

# 1. Make three Lists for Employee's Name , Employee's Department and Employee's salary.
# 2. Take input from user and add it to its specific list using "append function".
# 3. Now using "range function in for loop" print all the specific lists.
# 4. Now using "descending order sorting function" print the list in descending order.
# 5. Make two new variable for storing highest and lowest values.
# 6. Again make two new variables for storing postion of highest and lowest values using "index functions".
# 7. And at last Print all the values by calling the variables which we had just created.


# Highest Salary and Lowest Salary :-

employName=[]
employDept=[]
employSalary=[]

for i in range(5):
    EmployName=input("Enter Employee's Name : ")
    employName.append(EmployName)

    EmployDept=input("Enter Employee's Department : ")
    employDept.append(EmployDept)
    
    EmploySalary=int(input("Enter Employees's Salary : "))
    employSalary.append(EmploySalary)

for i in range(len(employName)):
    print(i,employName[i],employDept[i],employSalary[i])

employSalary.sort(reverse=True)
HighestSalary=employSalary[0]
LowestSalary=employSalary[4]
HSemployName=employSalary.index(HighestSalary)
LSemployName=employSalary.index(LowestSalary)

print("Highest salary Employee Name , Department and Salary :",employName[HSemployName],employDept[HSemployName],employSalary[HSemployName])
print("Lowest salary Employee Name , Department and Salary :",employName[LSemployName],employDept[LSemployName],employSalary[LSemployName])
