import numpy as np
id=input("เลขบัตรประชาชน12หลัก = ")
l=list(id[:12])
a=np.array(l,dtype=int)
b=np.arange(13,1,-1)
x=np.sum(a*b)%11
if x<=1:
    d=1-x
else:
    d=11-x
e=np.sum(a*b)+d
f=e%11

def id_check(id):
    l=list(id[:12])
    a=np.array(l,dtype=int)
    b=np.arange(13,1,-1)
    x=np.sum(a*b)%11
    return
    if x<=1:
        d=1-x
    else:
        d=11-x
print(*a,d)