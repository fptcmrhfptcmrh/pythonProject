import sys
input=sys.stdin.readline 
dic={}
s=open('C:/Users/windows/Desktop/python/엘니뇨라니냐예측 - 2학년 지구과학 스행/nino3.4.txt')
for _ in range(154):
    k=list(map(float,s.readline().split()))
    dic[int(k[0])]=k[1:]
print(dic)