
#Write a Program to deletion of last item, deletion of item by position, Addition of item to in the list at last, Addition of item By position In the List , New list with all same items as previous list,Deleting all the items from the list, Deleting the Whole List for Given item from the List :-


#Functions to be performed in Given List :-

#Deletion Of Last Item from the given list Using "pop function".
#Deletion of Item by choosing the position from the given list using "pop(position) function".
#Adding the new Item that user wants to add in the given list using "append function".
#Adding the new item that user wants to add in a specific position in the given list using "insert function".
#Making of new list if their is any changes in old list that change must be reflected on new list using "copy function".
#Clearing the all Items from the list using "clear function".
#Deleting the given list using "del function".


Grocery=[]
#Deletion of Items from List :-

for i in range(10):
    AGR=input("Enter grocery items :-")
    Grocery.append(AGR)
    
print("Before Deletion of Item from List :-")
l=len(Grocery)
for i in range(l):
    print(i,Grocery[i])


#Deletion Of Last Item from the given list Using "pop function".
    
print("Deletion of Last Item from list :-")
Grocery.pop()
l1=len(Grocery)
for i in range(l1):
    print(i,Grocery[i])


#Deletion of Item by choosing the position from the given list using "pop(position) function".
    
print("Deletion of item by choosing position from list :-")

chooseItemDel=int(input("Enter The position of Item that you want to delete  from list :- "))
Grocery.pop(chooseItemDel)
l2=len(Grocery)
for i in range(l2):
    print(i,Grocery[i])


#Adding the new Item that user wants to add in the given list using "append function".

add=input("Enter the Item Name You want to add :-")
Grocery.append(add)
l3=len(Grocery)
for i in range(l3):
    print(Grocery[i])


#Adding the new item that user wants to add in a specific position in the given list using "insert function".
    
addPos=int(input("Enter the Item Positon You want to add with Position :-"))
addPosName=input("Enter the Grocery Item you want to add :-")
Grocery.insert(addPos,addPosName)
l4=len(Grocery)
for i in range(l4):
    print(Grocery[i])


#Making of new list if their is any changes in old list that change must be reflected on new list using "copy function".
    
print("Creating New list for future upgradation :-")
NewList=Grocery
lN=len(NewList)
Grocery.append('Stationary')
for i in range(lN):
    print(NewList[i])


#Clearing the all Items from the list using "clear function".
    
print("Deleting the all Items from List :-")
Grocery.clear()
print(Grocery)


#Deleting the given list using "del function".

print("Deleting the  Whole List :-")
del Grocery
print(Grocery)


#Write a program to add at last , add at position , delete at last , delete at position , deleting the elements , deleting the list   from the  Given List.
