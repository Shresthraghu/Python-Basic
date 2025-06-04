# Two friends listed thier hobbies.

# Write a program to find out which which hobbies they have commom.

suresh=["Dancing","Singing","Reading books","Photography","Playing Cricket","Travelling","Swimming","Running","Playing Video Games"]
ramesh=["Playing Video Games","Playing Football","Dancing","Skipping","Drawing","Art and Craft","Yoga","Meditation"]

print("\nList of hobbies of suresh :-\n")
for i in range(len(suresh)) :
    print(i,suresh[i])


print("\nList of hobbies of ramesh :-\n")
for i in range(len(ramesh)) :
    print(i,ramesh[i])

s=set(suresh)
r=set(ramesh)

s.intersection_update(r)

print("\nList of common hobbies of both friends :-\n")
for i in s :
    print(i)
