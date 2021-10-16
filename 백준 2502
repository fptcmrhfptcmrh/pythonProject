#coding=utf-8
'''
뭐적을지 모르겠으니까 나중에 적어야 겠다
'''
def asdf(p):
    k = [1, 1]
    for i in range(2, p + 1):
        k.append(k[i - 1] + k[i - 2])  # k[i]=k[i-1]+k[i-2]
    return k[p-1], k[p]

n=0
m=0
j=0
q = input().split()
a = int(q[0])
b = int(q[1])
e,r=asdf(a-2)
for i in range(b//e):
    if (b-i*e)%r==0:
        j=(b-i*e)//r
        if e*i+r*j == b:
            if i<j:
                n=i
                m=j
                break
print(n)
print(m)
