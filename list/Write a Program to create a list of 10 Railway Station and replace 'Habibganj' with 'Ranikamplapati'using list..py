#Write a Program to create a list of 10 Railway Station and replace 'Habibganj' with 'Ranikamplapati'using list.
#10 Railway Stations.

RS=[]
RS=['Bhopal Junction','Vidisha Station', 'Sagar Station','Habibganj','Indore Junction','Bina Station','Ratlam Junction','Gwalior Junction','Satna Junction','Sanchi Station','Rewa Station']
l=len(RS)
print("Before Upgradation of List : ")
for i in range(l):
    print(i,RS[i])
print("After Upgradation of List : ")
RS[3]='Ranikamlapati'
for i in range(l):
    print(i,RS[i])






