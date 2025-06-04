# Two mobile apps track thier users.

# Write a program to find users who are using only one of the two apps , not both.

App1=["Ajay Devgn","Bobby Deol","Chunky Pandey","Dilip Kumar","Emraan Hashmi","Farhan Akhtar","Guru Dutt","Harshvardhan Rane","Virat Kholi","Rajat Sharma","Amitabh Bachan"]
App2=["Ajay Devgn","Bobby Deol","Chunky Pandey","Dilip Kumar","Emraan Hashmi","Kareena Kapoor","Katrina Kaif","Anushka Sharma","Hardik Pandya","Abhishek Bachan","Dolly Chawla"]

print("\nList of customers who uses App1 :-\n")
for i in range(len(App1)):
    print(i,App1[i])

print("\nList of customers who uses App2 :-\n")
for i in range(len(App2)):
    print(i,App2[i])

A1=set(App1)
A2=set(App2)
A1.symmetric_difference_update(A2)

print("\nList of users who are using only one of the two apps , not both :-\n")

for i in A1:
    print(i)
