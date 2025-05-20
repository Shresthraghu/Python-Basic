# Student Result Evaluation

# A school system determines pass/fail based on attendance and average marks. If attedance is below 75%,the student automatically fails. If attendance is good but marks are below 60% they need remedial classes .

attendance=int(input("Enter Student's attendance : "))
avgMarks=int(input("Enter Student's Average Marks : "))

if(attendance>75):
    if(marks<60):
        print("Student needs remedial classes.")
    else:
        print("Student is passed.")
else:
    print("Student is failed.")
