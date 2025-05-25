# Write a program to check if a number is a power of 2 using bitwise operations .

# Checking if a number is a power of 2 :-

n=int(input("Enter any number : "))
if ((n&(n-1))==0):
    print(n,"is a power of 2. ")
else:
    print(n,"is not a power of 2. ")
