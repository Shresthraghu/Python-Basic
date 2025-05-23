pro=['cooler','ac','fridge','WC','radio']
qty=[12,45,31,34,5]
nwqty=qty.copy()
nwqty.sort(reverse=True)
print(pro)
print(qty)
print(nwqty)
hval=nwqty[0]
lval=nwqty[4]
hval1=qty.index(hval)
lval1=qty.index(lval)
print("city with highest value",pro[hval1],qty[hval1])
print("city with lowest value",pro[lval1],qty[lval1])    

