#Write a program to enter 10 Products Name and its quantity , find out product with Highest Quantity and Product Name , and Lowest Quantity and Product name . 

#Product name and quantity :-

name=[]
quantity=[]

for i in range(10):
    ProdName=input("Enter Product Name : ")
    name.append(ProdName)
    ProdQuan=int(input("Enter the product Quantity : "))
    quantity.append(ProdQuan)

print("S.no  Product Name  Product Quantity")
for i in range(len(name)):
    print(i,name[i],quantity[i])


print("After sorting :-")
quantity.sort(reverse=True)
HighVal=quantity[0]
LowVal=quantity[9]
HighVal1=quantity.index(HighVal)
LowVal1=quantity.index(LowVal)

print("Highest Sold Product Name : ",name[LowVal1])
print("Highest Sold Product Quantity : ",quantity[HighVal1])
print("Lowest Sold Product Name : ",name[HighVal1])
print("Lowest Sold Product Quantity : ",quantity[LowVal1])
