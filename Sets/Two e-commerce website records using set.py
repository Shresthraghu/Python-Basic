# Two e-commerce website recorded  their regular customers.

# Website A has a list of its regular customers.
# Website B has it's own list.

# Write a program to find out which customers are common to both the websites.

webA={"Suresh","Rajesh","Jayesh","Mahesh","Ritesh","Amitesh","Nigesh","Ramesh"}
webB={"Nigesh","Jayesh","Surendra","Mahendra","Shailendra","Raghuvendra","Narendra"}

print("Regular Customers List from Website A :-")
for i in webA :
    print(i)

print("Own List Customers from Website B :-")
for i in webB :
    print(i)

webC=webA.intersection(webB)
print("Common Customers from both the websites are : ",webC)
                  


