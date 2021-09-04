def two (ans):
    k=[]
    powlist=[8,4,2,1]
    for i in range(4):
        if int(ans/powlist[i])==1:
            k.append("딸기")
            ans-=powlist[i]
        else:
            k.append("V")
    return k
def two2 (ans):
    k=[]
    powlist=[8,4,2,1]
    for i in range(4):
        if int(ans/powlist[i])==1:
            k.append("V")
            ans-=powlist[i]
        else:
            k.append("딸기")
    return k
def asdf(ans):
    if ans%28<=15 and ans%28!=0:
        ansk=ans%28
        return two(ansk)
    elif ans%28==0:
        return two(2)
    else:
        ansk=30-ans%28
        return two(ansk)
time=int(input())
for i in range(time):
    ans=int(input())
    ans2=ans
    ansp=asdf(ans)
    anskk="".join(ansp)
    print(anskk)
    
