import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
image=Image.open("해안선의 역설 - 2학년 세특\WHITE_MAP.jpg")
img_np=np.array(image)
width,height=image.size
lst=[]
def func(lst,i,j,n):
    for x in range(i,i+n):
        for y in range(j,j+n):
            if lst[y][x]!=255:
                return 1
    else: return 0
for i in img_np:
  l=[]  
  for j in i:
    l.append(j[0])
  lst.append(l)
ans=[]
for n in range(3,301):
    sm=0
    for i in range(0,width-n,n):
        for j in range(0,height-n,n):
            sm+=func(lst,i,j,n)
    ans.append(sm*n)
    print(sm*n)
x_var=[i for i in range(3,301)]
x=np.arange(len(x_var))
plt.bar(x,ans,width=1.0)
plt.xticks(x,x_var)
plt.show()
