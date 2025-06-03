nm1=['anu','renu','monu','sonu','divya']
nm2=['pooja','lata','jeetu','sonu']
nm3=['anu','renu','monu']
nm1=set(nm1)
nm2=set(nm2)
nm3=set(nm3)
print(nm1)
print(nm2)
print(nm3)
an=nm1.issuperset(nm3)
print(an)
an=nm3.issubset(nm1)
print(an)
nm3.clear()
print(nm3)
nm4=nm1.union(nm2)
print(nm4)

