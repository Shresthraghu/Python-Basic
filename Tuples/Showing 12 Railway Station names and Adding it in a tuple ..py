# Write a program to show a tuple which consits of 12 Railway Stations to a user and if he wants to add it to add it or remove it . Convert the tuple into list for modifications and again convert the list into tuple.

# Showing 12 Railway Station names and Adding it in a tuple.


RS=('Bhopal Junction','Vidisha Station', 'Sagar Station','Habibganj','Indore Junction','Bina Station','Ratlam Junction','Gwalior Junction','Satna Junction','Sanchi Station','Rewa Station','ahemdabad junction')
for i in range(len(RS)):
    print(i,RS[i])

Add=input("Do you want to add Railway Station Names ?")

if(Add!="Yes" or Add!="YES" or Add!="yes"):
    ARS=[]
    ARS=list(RS)
    add=input("Enter the Railway Station name ")
    Pos=int(input("At which Position you want to add the name?"))
    ARS.insert(Pos,add)
    RS=tuple(ARS)
    for i in range(len(RS)):
        print(RS[i])
     break   
    

    add1=input("Do you want to add Railway Station Names ?")
    if(Add=="Yes" or Add=="YES" or Add=="yes"):
        add=input("Enter the Railway Station name ")
        Pos=int(input("At which Position you want to add the name?"))
        ARS.insert(Pos,add)
        RS=tuple(ARS)
        for i in range(len(RS)):
            print(RS[i])
        pos=RS.index('Sagar Station')
        print("This Railway station name has been add it twice.",pos)

    else:
        RS=tuple(ARS)
        for i in range(len(RS)):
            print(RS[i])
    
    
else:
    print("Since user wants no upgradation in Railway station List .")
    for i in range(len(RS)):
        print(i,RS[i])

          

    
    
