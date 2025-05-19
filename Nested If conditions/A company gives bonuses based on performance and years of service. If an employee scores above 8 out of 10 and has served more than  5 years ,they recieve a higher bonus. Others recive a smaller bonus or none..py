# A company gives bonuses based on performance and years of service. If an employee scores above 8 out of 10 and has served more than  5 years ,they recieve a higher bonus. Others recive a smaller bonus or none.

# Employee Bonus :-

Performance=int(input("Enter employee's Performance out of 10 : "))
Served=int(input("How many years Employee has served : "))

if(Performance>=9):
    if(Served>5):
        print("Employee will recieve a Higher Bonus ")
    else:
        print("Employee has served less than 5 years , Employee will get a smaller bonus .")
elif(Performance>=8):
    if(Served>4):
        print("You will recieve a Smaller Bonus")
    else:
        print("Employee has served less than 4 years , Employee will get a no bonus .")
else:
    print("Employee Performance is not upto the mark ,Employee will recieve no bonus")
