# Write a program to create a list of having names of player who plays Basketball , now make second List of players who plays football and make another list of players who plays cricket .Find out how the names of player who plays only basket ball,find out names of players who plays all the games and names of players who plays only one game .

# List of Players using sets :-

BB=["Sonu","Monu","Rajat","Somesh","Ritesh"]
FB=["Shailendra","Surendra","Somesh","Ritesh","Mahesh"]
CKT=["Rajesh","Surendra","Somesh","Nigesh","Prashant"]


SBB=set(BB)
SFB=list(FB)
SCKT=list(CKT)

SBB.difference_update(SFB)
SBB.difference_update(SCKT)
print("Players who only plays basket ball : ",SBB)



PBB=set(BB)
PFB=set(FB)
PCKT=set(CKT)

PBB.intersection_update(PFB)
PBB.intersection_update(PCKT)
print("Players who plays all the games : ",PBB)



RBB=set(BB)
RFB=set(FB)
RCKT=set(CKT)

RBB.symmetric_difference_update(RFB)
RFB.symmetric_difference_update(RCKT)
print("Players who plays only on game : ",RFB)



