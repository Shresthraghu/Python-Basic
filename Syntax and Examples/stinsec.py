# Printing common element from both the sets.

# syntax : set1.intersection_update(set2)

nm1=['Anu','Renu','Monu','Sonu']
nm2=['Chiya','Anu','Pooja','Lata']
nm1=set(nm1)
nm2=set(nm2)
print(nm1)
print(nm2)
nm1.intersection_update(nm2)
print(nm1)
print(nm2)

