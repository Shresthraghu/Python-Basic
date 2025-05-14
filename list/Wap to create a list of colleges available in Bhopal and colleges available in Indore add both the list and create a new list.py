#Write a program to create a list of colleges available in Bhopal and colleges available in Indore add both the list and create a new list.
#Colleges List

Bplcol=['Lnct','Bansal','Oriental','TIT','Sam','RKDF','RGPV','Sirt','SIStech','IES','Patel Group of Institutes']
Bpllen=len(Bplcol)
Indbcol=['IIST','Acropolis','Govindram Seksaria','Aurbindo','SAGE University','VITM','Prestige Institute','Astral Group','Dr A.P.J Abdul Kalam University','Vaishnav Polytechnic','Symbiosis']
Indblen=len(Indbcol)
print("Before Merging Both the Lists :-")
print("Colleges in Bhopal :-")
for i in range(Bpllen):
    print(i,Bplcol[i])
print("Colleges in Indore :-")
for i in range(Indblen):
    print(i,Indbcol[i])    
allcol=Bplcol+Indbcol
allcollen=len(allcol)
print("After Merging Both the Lists :-")
print("All the colleges in Bhopal and Indore are :-")
for i in range(allcollen):
    print(i,allcol[i])
