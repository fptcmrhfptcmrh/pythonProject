import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
image=Image.open("D:\pyhton_pr\프랙탈 길이 - 2학년 수학수행\WHITE_MAP.jpg")
img_np=np.array(image)
width,height=image.size
lst=[]
for i in img_np:
  l=[]  
  for j in i:
    l.append(j[0])
  lst.append(l)
print(len(lst[0:3]))
print(len(lst[0:3][0:3]))
# print(np.array(image.crop((1500,0,1700,200))))
# for i in range(5,200):
# plt.imshow(img_np)
# plt.show()