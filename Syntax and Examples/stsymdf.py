# Removing common element from both the sets and merging both the rest of sets into a new set.

# syntax : nm3=nm1.symmetric_difference(nm2)

nm1=['Anu','Renu','Monu','Sonu']
nm2=['Chiya','Anu','Pooja','Lata']
nm1=set(nm1)
nm2=set(nm2)
print(nm1)
print(nm2)
nm3=nm1.symmetric_difference(nm2)
print(nm1)
print(nm2)
print(nm3)
