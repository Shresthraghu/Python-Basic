#Write a Program to create a data for 10 persons from users having age ,name and nationality and state the voting status.
#Election Criteria in list using nested If - else conditions.

name=[]
age=[]
nationality=[]
ele=[]
for i in range(5):
    NAME=input("Enter Your Name : ")
    name.append(NAME)
    
    AGE=int(input("Enter your age: "))
    age.append(AGE)
    
    NATIONALITY=input("Enter your nationality : ")
    nationality.append(NATIONALITY)
    
for i in range(len(age)):
    if(age[i]>=18):
        if(nationality[i]=='indian' or nationality[i]=='INDIAN'):
            ele.append("eligible")
        else:
            ele.append("Not eligible, Nationality issue")
    else:
        ele.append("Not eligible, Age issue")
print("name age nationality elegible")
for i in range(len(name)):
    print(name[i],age[i],nationality[i],ele[i])
    
