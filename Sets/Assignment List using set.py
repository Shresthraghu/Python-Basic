# A Teacher has a list of all students enrolled in a class and a list of those who submitted the latest assignment .

# Write a python program to find out which students did not submit the assignment .


enrolledStud={"Anshul","Bhavna","Chayya","Deepak","Ekta","Faizan","Gayatri","Harsh","Inteqam","Jack","Karan","Lavanya","Manish","Nitin","Om","Prashant","Qureshi","Raghuvendra","Suraj","Tanushree","Urvashi","Vikram","Wayankd","Xenom","Zaid"}
LatestStud={"Gayatri","Deepak","Inteqam","Karan","Zaid","Manish"}

print("\nEnrolled Students List :-\n")
for i in enrolledStud:
    print(i)
    
print("\nStudents List who submitted Latest assignment :-\n")
for i in LatestStud:
    print(i)


enrolledStud.difference_update(LatestStud)

print("\nList of studens who has not submitted the assignments :-\n")
for i in enrolledStud:
    print(i)
