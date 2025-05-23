a=int(input("Enter First no"))
b=int(input("enter Second No"))
if(a>10):
    if(b<10):
        c=a+b
        print("Sum is",c)
    else:
        print("Second no is not less than 10",b)
else:
    print("First no is not less than 10",a)
