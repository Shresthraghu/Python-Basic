stu={
    'nm':['Anu','renu','pooja'],
    'cls':12,
    'phy':90,
    'che':89,
    'mat':78
    }
print(stu)
print("--------------------")
print(stu['nm'])
nam=stu['nm']
print(nam)
nam1=stu.get('nm')
print(nam1)
ky=stu.keys()
print(ky)
vl=stu.values()
print(vl)
it=stu.items()
print(it)
for k,v in it:
    print(k,v)
for i in stu:
    print(i)
