def sum(a,b):
    c=a+b
    return c
def fun(a,b):
    a=a+10
    b=b+10
    return(a,b)

a=10
b=20
c=sum(a,b)
print("Sum is",c)
a1,b1=fun(a,b)
print(a1," ",b1)
c1=fun(a,b)
print("result is",c1)