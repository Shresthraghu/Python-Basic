# Write a program to enter your ACcount Number print it in a following manner.
#Account Number
interACC=input("Enter your Account Number")
iA=interACC[0:5]
iB=interACC[9:]
iD=iA+"XXXX"+iB
print(iD)
