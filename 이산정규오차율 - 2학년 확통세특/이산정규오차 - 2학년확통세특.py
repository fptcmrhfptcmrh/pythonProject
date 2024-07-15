import matplotlib.pyplot as plt 
import numpy as np 
from scipy.stats import norm 
from math import comb,sqrt
#정규분포 구현
err_lst=[]
for cnt in range(10,1000): #시료의 개수
    #m=cnt/2  sig=sqrt(cnt/4)
    err_sum,err_per=0,0
    mul_var=0.5**cnt
    for i in range(cnt+1):
        bi_var=comb(cnt,i)*mul_var
        if i==0 or i==cnt: nor_var=norm(cnt/2,sqrt(cnt/4)).cdf(0)
        else: nor_var=norm(cnt/2,sqrt(cnt/4)).cdf(i+1)-norm(cnt/2,sqrt(cnt/4)).cdf(i)
        err_sum+=abs(bi_var-nor_var)
    err_per=err_sum/cnt
    print(err_per)
    err_lst.append(err_per)
x=np.arange(990)
plt.bar(x,err_lst,width=1)
plt.show()