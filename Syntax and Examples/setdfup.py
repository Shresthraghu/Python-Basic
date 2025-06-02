# Removing common element from both the sets and implementing in the set itelf.

# variable name : set1.difference_update(set2)

nm1=['Anu','Renu','Monu','Sonu']
nm2=['Chiya','Anu','Pooja','Lata']
nm1=set(nm1)
nm2=set(nm2)
print(nm1)
print(nm2)
nm1.difference_update(nm2)
print(nm1)
print(nm2)

