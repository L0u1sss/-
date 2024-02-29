import numpy as np
y=input().split()
l=list(y[:7])
a=np.array(l,dtype=int)
b=np.sum(a)
print(b)