# A company launched a project in two regions . You are given sets of customers from Region A and Region B.

# Write a python program to find customers who bought the product only in Region A.

RegionA=["Satyendra","Mahendra","Raghuvendra","Shailendra","Amrendra","Narendra","Mahesh","Suresh","Ramesh","Hitesh","Vignesh","Naresh","Ritesh","Dipessh"]
RegionB=["Satyendra","Mahendra","Raghuvendra","Shailendra","Amrendra","Narendra","Tanisha","Manisha","Nitisha","Disha","Lapiksha","Esha","Nisha","Shirisha"]

print("\nList of customers from Region A :-\n")
for i in range(len(RegionA)):
    print(i,RegionA[i])


print("\nList of customers from Region B :-\n")
for i in range(len(RegionB)):
    print(i,RegionB[i])


A=set(RegionA)
B=set(RegionB)

A.difference_update(B)


print("\nList of customers who bought the product only in Region A :-\n")
for i in A:
    print(i)

