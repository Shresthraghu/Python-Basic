#Write a program to enter Age and Nationality of a person allow him to vote if person is not minor and if of Indian origin. 
#Criteria for Voting :-

age=int(input("Enter your age:"))
nationality=input("Enter your nationality:")
if(age>=18 and nationality=='indian'):
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

