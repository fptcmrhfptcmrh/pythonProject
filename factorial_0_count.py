count2=0
count5=0
count10=0
n=int(input())
for i in range(1,n+1):
    k=i
    while k>=5:
        if k%5==0:
            count5 += 1
            k//=5
            if k<5:
                break
        else:
            break

print(count5)
