x=input().split("/")
D = int(x[0])
M = int(x[1])
Y = int(x[2])
K = ["January" , "February" ,  "March" , "April" , "May" , "June" , "July" , "August" , "September" , "October" , "November" , "Demcember"]
print(K[M-1],D,Y)