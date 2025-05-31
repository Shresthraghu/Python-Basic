st={'anu','renu','monu','anu'}
for i in st:
    print(i)
print(st)
st1=set()
print(st1)
st1.add("Preeti in st1")
print(st1)
st1.update(st)
print(st1)

st.discard('renu')
print(st)
st=list(st)
print(st)
st.remove('anu')
print(st)
