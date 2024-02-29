import numpy as np
U = input().split(',')
V = input().split(',')
float_U = list(np.float_(U))
float_V = list(np.float_(V))
v3 = [float_U[0]+float_V[0], float_U[1]+float_V[1], float_U[2]+float_V[2]]
print(float_U,'+',float_V,'=',v3)