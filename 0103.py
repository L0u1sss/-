import math
a = float(input())
b = float(input())
c = float(input())
d = (b**2) - (4*a*c)
if d>0:
    sol1 = (-b-math.sqrt(d))/(2*a)
    sol2 = (-b+math.sqrt(d))/(2*a)
    print("คำตอบคือ {0} และ {1}".format(sol1,sol2))
else:
    print("ไม่มีคำตอบ")