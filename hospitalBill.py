#hospital bill:-

patientName=(input("Enter Patient Name :"));
unicode=int(input("Enter Unique Code :"));
ndays=int(input("Enter number of days stayed in hospital :"));
diag=int(input("how many diagnalysis test have done :"));
dayschar=(ndays*1000);
diagchar=(diag*5000);
totalamt=(dayschar+diagchar);
totalamt1=(((totalamt)*18)/100);
print("Patient name:" ,patientName);
print("Unique Code" ,unicode);
print("number of days stayed in hospital  :" ,ndays);
print("diagnalysis test have done :" ,diag);
print("Number of days charges:" ,dayschar);
print("diagonalysis charges :" ,diagchar);
print("total charges :" ,totalamt);
print("total charges with gst :" ,totalamt1);
                 
