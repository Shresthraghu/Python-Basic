# A Telecom Company wants to identify if a customer's monthly charges are above Rs 1,000 and they are on a month-to-month contract,flag them as high risk . Otherwise determine risk based on thier contract type .


# Task to perform :-

# 1. First Take charges as input from user.
# 2. Then check there charges.
# 3. If charges are more than Rs 1,000 flag them as Month-to-Month contract customer.
# 4. If charges are less than Rs 1,000 then ask their type of recharge from customer.
# 5. Based on thier type of recharge , print appropriate message.


# Customer Charges using Nested if:-


charge=int(input("Enter your monthly Telecom charges : "))
if(charge<1000):
   typeOfRec=input("Enter your type of recharge : ")
   if(typeOfRec=="monthly"):
     print("High risk customer .")
   elif(typeOfRec=="half yearly"):
     print("Low risk customer .")
   elif(typeOfRec=="annualy"):
     print("No risk customer .")
else:
    print(" Month-to-Month contract customer")
