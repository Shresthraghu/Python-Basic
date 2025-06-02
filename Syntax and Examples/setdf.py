# Removing common element from both the list and implementing in first List.

nm1=['Anu','Renu','Monu','Sonu']
nm2=['Chiya','Anu','Pooja','Lata']
nm1=set(nm1)
nm2=set(nm2)
print(nm1)
print(nm2)
nm3=nm1.difference(nm2)
print(nm1)
print(nm2)
print(nm3)
