#Write a program to create a list of Stationary Purchased by you and check if a given item is available or not.
#Stationary List:-

SL=['Pen','Pencil','Sharpner','Stapler','Eraser','Scale','Geometry Box','Fountain Pen','Black Pen','Red Pen','Sketch Pen','Highlighter','Crayon Colors','Clay','Notebooks','Diary','Slambook','Scrapbook','Artpapers','Register','Accountbook','Notepad','Glue gun','Glue stick']
print(SL[:7])
print(SL[8:14])
print(SL[15:21])
SLlen=len(SL)
for i in range(21):
    print(i,SL[i])
purchase=[]
for i in range(1):
    choose=input("Which Stationary item you would like to purchase :")
    purchase.append(choose)
print("You have purchased below items :-") 
print(purchase)
f=0
for i in SL:
    if(i==choose):
        f=1
        break
if(f==0):
    print("This Stationary Item is not available.")
else:
    print("This Stationary Item is available.")

     

    
