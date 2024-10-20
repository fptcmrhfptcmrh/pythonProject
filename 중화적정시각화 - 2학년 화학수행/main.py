import pygame,random,time
a,b=map(int,input().split())
pygame.init()
screen=pygame.display.set_mode([400,800])
running,falling=True,True
water=pygame.draw.rect(screen,(0,0,255),[0,500,400,300])
naohIl=pygame.image.load('C:/Users/windows/Desktop/python/중화적정시각화 - 2학년 화학수행/naoh.png')
black=pygame.image.load('C:/Users/windows/Desktop/python/중화적정시각화 - 2학년 화학수행/black.png')
h3oIl=pygame.image.load('C:/Users/windows/Desktop/python/중화적정시각화 - 2학년 화학수행/h3o.png')
ohIl=pygame.image.load('C:/Users/windows/Desktop/python/중화적정시각화 - 2학년 화학수행/oh.png')
naIl=pygame.image.load('C:/Users/windows/Desktop/python/중화적정시각화 - 2학년 화학수행/na.png')
clIl=pygame.image.load('C:/Users/windows/Desktop/python/중화적정시각화 - 2학년 화학수행/cl.png')
blue=pygame.image.load('C:/Users/windows/Desktop/python/중화적정시각화 - 2학년 화학수행/blue.png')
naoh2,h3o2,oh2,na2,cl2=[],[],[],[],[]
for _ in range(a*b):
    h3o=pygame.Rect(h3oIl.get_rect())
    h3o.left,h3o.top,dx,dy=random.randint(0,385),random.randint(515,785),1,1
    h3o2.append([h3o,dx,dy])
    cl=pygame.Rect(clIl.get_rect())
    cl.left,cl.top,dx,dy=random.randint(0,385),random.randint(515,785),-1,1
    cl2.append([cl,dx,dy])
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                naoh=pygame.Rect(naohIl.get_rect())
                naoh.left,naoh.top=200,0
                naoh2.append(naoh)
                print(naoh2)
    for naoh in naoh2:
        screen.blit(black,naoh)
        naoh.top+=2
        screen.blit(naohIl,naoh)
        if naoh.colliderect(water):
            naoh2.remove(naoh)
            screen.blit(black,naoh)
            na=pygame.Rect(naIl.get_rect())
            na.left,na.top,dx,dy=200,500,1,1
            na2.append([na,dx,dy])
            oh=pygame.Rect(ohIl.get_rect())
            oh.left,oh.top,dx,dy=200,500,-1,1
            oh2.append([oh,dx,dy])
    for i in range(len(h3o2)):
        h3o,dx,dy=h3o2[i]
        screen.blit(blue,h3o)
        if h3o.left+dx>=385 or h3o.left+dx<=0: dx*=-1
        if h3o.top+dy<=500 or h3o.top+dy>=785: dy*=-1
        h3o.left+=dx
        h3o.top+=dy
        h3o2[i]=[h3o,dx,dy]
        screen.blit(h3oIl,h3o)
    for i in range(len(oh2)):
        oh,dx,dy=oh2[i]
        screen.blit(blue,oh)
        if oh.left+dx>=385 or oh.left+dx<=0: dx*=-1
        if oh.top+dy<=500 or oh.top+dy>=785: dy*=-1
        oh.left+=dx
        oh.top+=dy
        oh2[i]=[oh,dx,dy]
        screen.blit(ohIl,oh)
    for i in range(len(na2)):
        na,dx,dy=na2[i]
        screen.blit(blue,na)
        if na.left+dx>=385 or na.left+dx<=0: dx*=-1
        if na.top+dy<=500 or na.top+dy>=785: dy*=-1
        na.left+=dx
        na.top+=dy
        na2[i]=[na,dx,dy]
        screen.blit(naIl,na)
    for i in range(len(cl2)):
        cl,dx,dy=cl2[i]
        screen.blit(blue,cl)
        if cl.left+dx>=385 or cl.left+dx<=0: dx*=-1
        if cl.top+dy<=500 or cl.top+dy>=785: dy*=-1
        cl.left+=dx
        cl.top+=dy
        cl2[i]=[cl,dx,dy]
        screen.blit(clIl,cl)
    del_lst=[]
    for i in range(len(oh2)):
        for j in range(len(h3o2)):
            oh,dx,dy=oh2[i]
            h3o,dx,dy=h3o2[j]
            if oh.colliderect(h3o): del_lst.append([i,j])
    for i,j in del_lst:
        screen.blit(blue,oh2[i][0])
        screen.blit(blue,h3o2[j][0])
        oh2.pop(i)
        h3o2.pop(j)
    pygame.display.update()
    time.sleep(0.002)
pygame.quit() 