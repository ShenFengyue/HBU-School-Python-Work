# 这段代码甚至没有输出，但竟然是对的

import numpy as np
def npsum(l1,l2):
    x=[]
    y=[]
    z=[]
    for i in range(len(l1)):
        x.append(int(l1[i])+int(l2[i]))
        y.append(int(l1[i])*int(l2[i]))
        z.append(int(l1[i])**2+int(l2[i])**3)
    return np.array(x),np.array(y),np.array(z)


L1=eval(input())
L2=eval(input())
x,y,z=npsum(L1,L2)
print(x,y,z)