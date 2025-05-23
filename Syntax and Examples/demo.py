c=0
while(True):
    a=int(input("Enter no"))
    if(a==0):
        c=c+1
        if(c>=3):
            break
    else:
        print(a)
    ans=input("Do you want to continue?")
    if(ans!='y'):
        break
