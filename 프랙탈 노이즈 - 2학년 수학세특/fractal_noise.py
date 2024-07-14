
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
f=open("pix.txt",'w')
im=Image.open("fractal_image.jpg")
pix=np.array(im).T[0]
print(pix)
print(im.size)
print(pix[1][3])
#640*360
x=np.arange(25)
y=np.arange(25)
print(x,y)
X,Y=np.meshgrid(x,y)
Z=pix[X][Y]
print(pix[1][2])
fig=plt.figure(figsize=(10,10))
ax=fig.add_subplot(111,projection='3d')
ax.scatter(X,Y,Z,marker='o',s=15)
plt.show()