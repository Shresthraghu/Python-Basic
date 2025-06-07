# Write a program to check the the number whether its even or odd from a list of numbers , if its even then do the square of that number using List.

# Checking if a Number in list is even and if its even then printing its square :-

nums=[1,2,3,4,5,6,7,8,9,10]
op=[x*2 for x in nums if x % 2!=0]
l=len(op)

print("\nPrinting Numbers in a List :-\n")
print(op)

print("\nPrinting Numbers Line by Line :-\n")
for i in range(l):
    print(i,op[i])

