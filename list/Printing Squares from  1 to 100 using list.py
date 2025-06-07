# Write a program to Create and print a list of squares from 1 to 100 .

squares=[x*x for x in range(101)]
l=len(squares)

print("\nPrinting in a List :-\n")
print(squares)

print("\nPrinting Line by Line :-\n")
for i in range(l):
    print(i,squares[i])

