#coding=utf-8
p1card=[1,2,3,4,5,6,7,8,9,10,11,12,13]
AIcard=[1,2,3,4,5,6,7,8,9,10,11,12,13]
def cardprint(player):
    if player=="p1":
        print(p1card)
    else:
        print(AIcard)
def playerchange(player):
    if player=="p1":
        return "AI"
    else:
        return "p1"
def isincard(ans,player):
    if player=="p1":
        if ans in p1card:
            return True
        else:
            return False
    else:
        if ans in AIcard:
            return True
        else:
            return False
def usedcard(ans,player):
    if player=="p1":
        p1card.remove(ans)
    else:
        AIcard.remove(ans)
def isempty ():
    global p1card
    global AIcard
    if len(p1card)==0 and len(AIcard):
        return False
    else:
        return True
def scoreplus(ansprev,anscur,player):
    if player=="p1":
        global p1score
        p1score+=abs(ansprev-anscur)
    else:
        global AIscore
        AIscore+=abs(ansprev-anscur)
def AIprocess(prevans):
    max=-1
    choosingcard=0
    global AIcard
    for i in range(0,len(AIcard)):
        if abs(int(AIcard[i])-prevans)>=max:
            max=abs(int(AIcard[i])-prevans)
            choosingcard=int(AIcard[i])
    return choosingcard
def AIprocess2(prevans):
    max=-1000
    choosingcard=0
    global AIcard
    global p1card
    for i in range(0, len(AIcard)):
        for j in range(0,len(p1card)):
            if abs(int(AIcard[i])-prevans)-abs(int(AIcard[i])-int(p1card[j]))>=max:
                max=AIcard[i]-p1card[j]
                choosingcard=AIcard[i]
    return choosingcard

""""
def AIprocess3(prevans,n,AIcard,p1card):
    choosingcard=0
    max=-100
    if n%2==0:
        for i in range(0, len(AIcard)):
            curAns=abs(prevans-AIcard[i])
            if n>=1:
                AIcard2 = AIcard.copy()
                nextScore, _ = AIprocess3(AIcard[i],n-1,AIcard2.remove(AIcard[i]),p1card)
                curScore = curAns-nextScore
                if curScore>=max:
                    max=curScore
                    choosingcard=AIcard[i]
        return max, choosingcard
    else:
        for i in range(0,len(p1card)):
            curAns=abs(prevans-p1card[i])
            p1card2 = p1card.copy()
            if n >= 1:
                nextScore, _ = AIprocess3(AIcard[i], n - 1, p1card2.remove(p1card[i]), p1card)
            curScore = curAns-nextScore
            if curScore>=max:
                max=curScore
                choosingcard=p1card[i]
        return max, choosingcard
"""

"""
    for i in range(0, len(AIcard)):
        for j in range(0,len(p1card)):
            if abs(int(AIcard[i])-prevans)-abs(int(AIcard[i])-int(p1card[j]))>=max:
                max=AIcard[i]-p1card[j]
                choosingcard=AIcard[i]
                AIcard.remove(choosingcard)
                p1card.remove()
                if n<=0:
                    return choosingcard
                else:
                    AIprocess3(choosingcard, n-1)"""

#main
player="p1"
previousAns = 7
p1score=0
AIscore=0
while isempty():
    print(player)
    cardprint(player)
    print(previousAns)
    while True:
        if player=="p1":
            currentAns=int(input("어떤 카드를 내시겠습니까?"))
        else:
            currentAns=AIprocess2(previousAns)
        if isincard(currentAns,player):
            break
        else:
            print("다시 입력해 주세요")
    scoreplus(previousAns,currentAns,player)
    usedcard(currentAns,player)
    print(p1score)
    print(AIscore)
    previousAns=currentAns
    player = playerchange(player)
print("game over")
if p1score>AIscore:
    print(" winner \n")
    print("   p1   ")
elif p1score==AIscore:
    print(" draw ")
else:
    print(" winner \n")
    print("   AI   ")



