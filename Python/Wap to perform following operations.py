#Write a Program to enter 2 numbers and perform the following operations and print all fields:-
#1.Add
#2.Subtract
#3.Multiply
#4.Modulus


FirstNum=int(input("Enter The First Number : "))
SecondNum=int(input("Enter The Second Number : "))
Add=(FirstNum + SecondNum)
Subtract=(FirstNum - SecondNum)
Multiply=(FirstNum * SecondNum)
Module=(FirstNum % SecondNum )
print("User Entered First Number : ",FirstNum)
print("User Entered Second Number : ",SecondNum)
print("After Addition of two Numbers thier value is : ",Add)
print("After Subtraction of two Numbers thier value is : ",Subtract)
print("After Multiplication of two Numbers thier value is : ",Multiply)
print("After Division of two Numbers thier value is : ",Module)
