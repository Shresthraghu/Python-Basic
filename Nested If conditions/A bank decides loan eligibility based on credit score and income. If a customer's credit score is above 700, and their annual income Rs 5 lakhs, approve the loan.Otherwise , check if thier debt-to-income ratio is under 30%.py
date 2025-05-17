# A bank decides loan eligibility based on credit score and income. If a customer's credit score is above 700, and their annual income Rs 5 lakhs, approve the loan. Otherwise , check if thier debt-to-income ratio is under 30%.


# Tasks to perform :-

# 1.First check their credit score is more than 700 using if condition.
# 2.If the Credit score is less than 700 ,then do not approve the loan and print the appropriate message .
# 3.If the Credit Score is more than 700 ,then check thier Annual Income.
# 4.If the Annual Income is less than 500,000 , then do not approve the loan and print the appropriate message.
# 5.If the Annual Income is more than 500,000 , then approve the loan an print appropriate message.
# 6.Otherwise check their Debt to income ratio is under 30% and print appropriate message.

# Loan Approval using Nested if:-

cs=int(input("Enter your credit score : "))

if(cs>700):
    ai=int(input("Enter your Annual Income : "))
    if(ai>500000):
        print("loan is approved.")
    else:
        print("Your Annual Income is less , loan is not approved.")
else:
    print("credit score is not more than 700")
    DTI=input("Your Loan is not approved , Do you want to check your Debt to income ratio ?")
    if(DTI=='Yes' or DTI=='YES' or DTI=='yes'):
        MonthlyDebt=int(input("Enter Your Total Monthly Debt : "))
        MonthlyInco=int(input("Enter Your Total Monthly Income : "))
        Ratio=((MonthlyDebt/MonthlyInco)*100)
        if(Ratio>300):
            print("Your Debt to Income ratio is more than 30%")
            print("Your Debt to Income ratio is more but your loan is also not approved.")
        else:
            print("Your Debt to Income ratio is less than 30%")
            print("Your Debt to Income ratio is less and your loan is also not approved.")
