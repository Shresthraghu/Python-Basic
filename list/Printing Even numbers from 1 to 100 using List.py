# Write a program to Create and print list of all even numbers from 1 to 100 .

evens=[x for x in range(101) if x % 2 == 0]
l=len(evens)

print("\nPrinting in a List :-\n")
print(evens)

print("\nPrinting Line by Line :-\n")
for i in range(l):
    print(i,evens[i])
