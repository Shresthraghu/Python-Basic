# A store offers a discount based on product category and volume sold . If the product is of electronics and more than 100 units are sold in a day , apply a 20% discount . Otherwise , apply a 10 % or 5 % discount based on product category .

# Discount Strategy :-

name=input("Enter Product name : ")
category=input("Enter product's Category : ")
units=int(input("How many units are sold ? "))

if(category=='electronics' and units>100):
    print("20 % Discount Applied.")

elif(category=='clothing' and units>90):
    print("10 % Discount Applied")
    
elif(category=='footwear' and units>80):
    print("5 % Discount Applied")    
           
else:
    print("Product category is not matched  , Discount is not applied.")


