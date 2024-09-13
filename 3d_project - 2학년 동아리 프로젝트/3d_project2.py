import numpy as np
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from PIL import Image
im=Image.open("first_modeling.png")
ppix=np.array(im).T[0]
pix,x,y=[],[],[]
for i in range(len(ppix)):
    k=ppix[i].tolist()
    r=[]
    for j in range(len(k)):
        m=1
        print(i,j,k[j])
        cnt=0
        for b in list(map(int,reversed(list(bin(k[j])[2:])))):
            if b==1: 
                pix.append(m)
                print(m)
                cnt+=1
            m+=1
        for _ in range(cnt):
            x.append(i)
            y.append(j)
x=np.array(x)
y=np.array(y)
z=np.array(pix)
print(x)
print(y)
print(z)
fig=plt.figure(figsize=(10,10))
ax=fig.add_subplot(111,projection='3d')
ax.scatter(x,y,z,marker='o',s=15000)
plt.show()