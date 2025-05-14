#Write a program to create a list of fruit items to be Purchase now replace any fruit item with any fruit item.
#Replacing fruit with another fruit in list.

fruit=['Apple','Banana','Chikoo','Dragaon Fruit','Grapes','Orange','Straw Berry','Water melon','Mango','Pineapple','Peach']
print(fruit)
newFruit=input("Which fruit you want to search : ")
f=0
for i in fruit:
    if(i==newFruit):
        f=1
        break
if(f==0):
    print("Available")
else:
    print("Not Available")
AddFruit=input("Enter Fruit Name you want to add : ")
repFruit=input("Enter Fruit Name you want to replce : ")
AddFruitpos=int(input("Enter Fruit position you want to add :"))
fruit[AddFruitpos]=AddFruit
print(fruit)
print("Added Fruit : ",AddFruit)
print("Replaced Fruit : ",repFruit)
