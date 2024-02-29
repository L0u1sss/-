x=input()
t1= x[3::7]
t2= x[7::5]
n3= int(t1) + int(t2) + 10000
t4= str(n3)[-4:-1]
n5= (int(t4[0])+int(t4[1])+int(t4[2])) % 10 + 1
t6= "ABCDEFGHIJ"[n5-1]
print(t4+t6)