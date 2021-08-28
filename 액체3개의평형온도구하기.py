#coding=utf-8
'''

다음주에 계속
to be continued
2021년 9월 첫째주 검사 

'''

anslist=list(input().split())
ac=float(anslist[0])  #a의 비열
bc=float(anslist[1])  #b의 비열
cc=float(anslist[2])
am=int(anslist[3])  #a의 질량
bm=int(anslist[4])  #b의 질량
cm=int(anslist[5])
at=int(anslist[6])  #a의 초기온도
bt=int(anslist[7])  #b의 초기온도
ct=int(anslist[8])
acm=ac*float(am)
bcm=bc*float(bm)
ccm=cc*float(cm)
print((acm*at+bcm*bt+ccm*ct)/acm+bcm+ccm)
