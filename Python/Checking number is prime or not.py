# Write a program to check a number is prime or not.

# Checking Number is prime or not :-

num=int(input("Enter any Number : "))
for i in range(2,int(num**0.5)+1):
        if(num%i==0):
           print(num,"is not a prime number.")
        else:
            print(num,"is a prime number.")     
                
                
