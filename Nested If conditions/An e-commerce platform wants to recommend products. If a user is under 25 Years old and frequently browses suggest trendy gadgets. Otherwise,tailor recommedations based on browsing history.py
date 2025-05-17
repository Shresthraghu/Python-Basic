# An e-commerce platform wants to recommend products. If a user is under 25 Years old and frequently browses suggest trendy gadgets. Otherwise,tailor recommedations based on browsing history .

# Tasks to be performed in this code :-

# 1. Take age input from user.
# 2. Now check if the age is equal or more than 25 .
# 3. If the age is equal to and less than 25 , then asks the user if he/she frequently browses or not.
# 4. If the user says yes then recommend the Trendy gadgets to the user.
# 5. If the user says no then recommend based on browsing history.
# 6. If the user is More then 25 then recommend based on browsing history.

# Product Recommendation using Nested if :-

age=int(input("Enter your age : "))

if(age<=25):
    browses=input("Do you Frequently browses ?")
    if(browses=='Yes' or browses=='YES' or browses=='yes'):
        print("You can go through our Trendy Gadgets :-")
        Trendy=['Portable Night Lamp' , 'Mini Table Cooler','Mini Fridge','Foldable Chair','Led lights','Disco Bulb' ]
        for i in range(len(Trendy)):
            print( i,Trendy[i])
    else:
        print("Based on your Browsing History you can go through on :- ")
    history=['Eggs','Dog Treats','Stationary','Plates','Tap','Soft Drinks','Bread','Napkins']
    for i in range(len(history)):
            print( i,history[i])

else:
    print("Based on your Browsing History you can go through on :- ")
    history=['Eggs','Dog Treats','Stationary','Plates','Tap','Soft Drinks','Bread','Napkins']
    for i in range(len(history)):
            print( i,history[i])
