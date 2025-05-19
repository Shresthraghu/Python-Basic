# Energy Usage Alert

# An Energy provider monitors household consumption. If monthly usage exceeds 1,000 kWh and the house doesn't use solar panels, send a high usage alert. If solar is present, suggest optimization tips.

Power=int(input("Enter the Power consumed in household in a month : "))
hour=int(input ("Enter the Hour consumed in household in a month : "))
kWh=((Power*hour)/1000)
print("Your Monthly Consumption is :",kWh)
solar=input("Do you use Solar Powers ?")

if(kWh>1000 and solar=="yes" or solar=="YES" or solar=="Yes" ):
    print("Solar Optimization Tips:-")
    print("1.Use Mirrors.")
    print("2.Keep the panels clean.")
    print("3.Minimizing Shading")
    print("4.Choose High-Efficency Panels.")

elif(kWh>1000 and solar=="no" or solar=="NO" or solar=="No" ):
    print("High Usage alert.")
        
elif(kWh<=1000 and solar=="yes" or solar=="YES" or solar=="Yes"):
    print("Low Usage alert")

else:
    print("Switched to advanced Solar Panels for saving consumption.")
