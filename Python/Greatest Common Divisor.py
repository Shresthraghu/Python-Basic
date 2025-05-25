# Write a  program to find the Greatest Common Divisor (GCD) of two numbers.

# Greatest Common Divisor (GCD):-

a=36
b=60
while b :
    a,b=b,a%b

print(a,b)
print("The common divisor of both the numbers is ",a)
