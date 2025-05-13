#Write a program to enter record of an product having Product Name , Code , Quantity and rate per product check if the total amount is in triple digit
#than if the total amount is not in triple digit. Calculate 10% discount,18% Gst and total amount and print all the fields . 

# Mall Bill :-

prodName=input("Enter Product name :")
prodCode=int(input("Enter Product's unique code :"))
prodQuan=int(input("Enter Product's Quantity :"))
ratePerProd=int(input("Enter rate per Product :"))
netAmt=(ratePerProd*prodQuan)
if(netAmt>99 and netAmt<1000):
    pass
else:
    disc=((netAmt*10)/100)
    finalamt=netAmt-disc
    gst=((finalamt*18)/100)
    totalAmt=(finalamt+gst)
    print("Product Name :",prodName)
    print("Product's Unique Code",prodCode)
    print("Product's Quantity :",prodQuan)
    print("Rate per Product is",ratePerProd)
    print("Your net amount is :",netAmt)
    print("with 10% discount amount is :",disc)
    print("18 % gst :",gst)
    print("Your total amount is",totalAmt)

