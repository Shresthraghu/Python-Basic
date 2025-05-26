#Write a program to create a list of Stationary Purchased by you and check if a given item is available or not.and store all the items in tuple .

# Stationary List in tuples :-

SL=('Pen','Pencil','Sharpner','Stapler','Eraser','Scale','Geometry Box','Fountain Pen','Black Pen','Red Pen','Sketch Pen','Highlighter','Crayon Colors','Clay','Notebooks','Diary','Slambook','Scrapbook','Artpapers','Register','Accountbook','Notepad','Glue gun','Glue stick')
for i in range(len(SL)):
    print(i,SL[i])

purchase=[]
avail=[]

while True :
    choose=input("Which Stationary item you would like to purchase : ")
    purchase.append(choose)
    if choose in SL :
        avail.append("not available")
    else:
        avail.append("available")

    Add=input("Do you want to purchase more stationary items ?")
    if Add != "yes":
        break
    
STpurchase=tuple(purchase)
STavil=tuple(avail)
print("You have purchased below items.")
for i in range(len(STpurchase)):
    print(i+1,STpurchase[i],":",STavil[i])
