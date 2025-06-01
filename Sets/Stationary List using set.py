# Write a program to create a list of Stationary items  further add more items to it .

# Stationary List using set :-

SL={'Notebooks','Chart Paper','HighLighter','Scale','Eraser','Sharpner','Pencil','Sketch Pen','Glue Gun'}
for i in SL:
    print(i)
while(True):
    add=input("Do you want to add more Stationary Items in list ?")
    if(add=="Yes" or add=="yes" or add=="YES"):
        Item=input("Enter the Stationary item name you want to add : ")
        SL.add(Item)
        for i in SL:
            print(i)
    else:
        print("User doesn't want to add items to the list.")
        break
