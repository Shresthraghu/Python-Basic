# write a program to cretae a list of having furniture available in your office and remove any duplicate.

# Furniture List using set :-

officeFur={'Table','stools','Chairs','Stools','computer Table','Sofa set','Almirah','computer Table','desks','stools','stools'}
print("Before removal of duplicates. ")
for i in officeFur:
    print(i)
    
UpofficeFur=list(officeFur)
UpofficeFur.remove('stools')
print("After removal of duplicates. ")
for i in UpofficeFur:
    print(i)

officeFur=set(UpofficeFur)
print("Now again converting list to sets")
l=len(officeFur)
for i in l:
    print(i,officeFur[i])
