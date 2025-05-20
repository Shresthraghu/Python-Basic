# Fraud Detection.

# A financial app flags suspicious Transactions.If a transactions exceeds Rs 10,000 and occurs outside the user's registered location, flag it as potential fraud . Otherwise ,require user verification.


Transactions=int(input("Enter  The Transactions Amount : "))
Location=input("Did the transaction occured outside Registered location : ")

if(Transactions>10000):
    if(Location=='yes' or Location=='Yes' or Location=='YES'):
        print("It's a potential fraud.")
    else:
        print("Its'a less potential fraud and requires user's verfication.")
else:
    print("No suspicious activity found .")
