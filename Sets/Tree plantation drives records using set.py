# Two NGOs conducted tree plantation drives and recorded names of participants in each in each event.

# Write a python program to find out which people participated in only one of the two drives but not both.

ANGO=["Aniket","Bhavya","Chetan","Dipesh","Eres","Farukh","Gyanedra","Hitesh","Isha","Jagdish","Kavya","Lavish","Monu","Nagralay","Omdev","Prakash","Qismat","Ricky","Satyam","Tarun","Umesh","Vijay","Wakim","Xerod","Zakhir"]
BNGO=["Aniket","Chetan","Eres","Gyanedra","Isha","Kavya","Monu","Omdev","Qismat","Satyam","Umesh","Wakim","Zakhir"]


print("\nPaticpants List of NGO A :-\n")
for i in range(len(ANGO)):
    print(i,ANGO[i])


print("\nPaticpants List of NGO B :-\n")
for i in range(len(BNGO)):
    print(i,BNGO[i])

A=set(ANGO)
B=set(BNGO)

A.difference_update(B)

print("\nParticipants List who had participated in only one of the two drives :-\n")
for i in A:
    print(i)
