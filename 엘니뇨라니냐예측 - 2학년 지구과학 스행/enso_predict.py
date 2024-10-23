import sys,pandas,datetime
import matplotlib.pyplot as plt
from scipy.stats import norm
input=sys.stdin.readline 
dic={}
s=open('C:/Users/windows/Desktop/python/엘니뇨라니냐예측 - 2학년 지구과학 스행/nino3.4.txt')
for _ in range(154):
    k=list(map(float,s.readline().split()))
    dic[int(k[0])]=k[1:]
avg=0
for i in dic:
    avg+=sum(dic[i])
avg/=154*12
ss=[]
for i in dic:
    k=[]
    for j in dic[i]:
        k.append(round(j-avg,2))
    ss=ss+k 
    dic[i]=k
a=pandas.date_range('18700101',datetime.date(2023,12,1),freq='MS')
x=[]
for i in range(len(a)):
    x.append(str(a.to_list()[i]).split()[0])
plt.plot(x,ss,color='blue',linestyle='-')
plt.show()
up,down=[],[]
for i in range(153):
    if ss[i]<ss[i+1]:
        up.append(ss[i+1]-ss[i])
    if ss[i]>ss[i+1]:
        down.append(ss[i+1]-ss[i])
upmax,upmin,downmax,downmin=round(max(up),2),round(min(up),2),round(max(down),2),round(min(down),2)
upavg,downavg=sum(up)/len(up),sum(down)/len(down)
a=float(input())
if a>=0.5: el="100"
elif a+upmax>=0.5: el=str(100*(1-norm.cdf(0.5-a,upavg,0.1)))#엘니뇨 가능성있음 
else: el="0"
if a<=-0.5: la="100"
elif a+downmin<=-0.5: la=str(100*(norm.cdf(-0.5-a,downavg,0.086))) #라니냐 가능성있음
else: la="0"
print("엘니뇨 : "+el+"%")
print("라니냐 : "+la+"%")
print(upavg,downavg,upmax,upmin,downmax,downmin)