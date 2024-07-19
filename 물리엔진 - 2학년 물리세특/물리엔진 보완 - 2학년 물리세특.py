import pygame,copy,math
pygame.init()
width,height=1500,910
ball_x,ball_y,ball_dx,size=750,21,0,10
click=False
drag_e,drag_s,ks,ke=0,0,0,0
screen=pygame.display.set_mode((width,height))
clock=pygame.time.Clock()
running=True
drag=False
start_time=pygame.time.get_ticks()
font=pygame.font.SysFont(None, 50)
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            ball_x,ball_y=pygame.mouse.get_pos()
            drag_s=copy.deepcopy(ball_x)
            click=True
            k=0
            drag=False
        elif event.type==pygame.MOUSEBUTTONUP:
            click=False
            start_time=pygame.time.get_ticks()
            drag=False
        elif event.type==pygame.MOUSEMOTION and click:
            drag_e=pygame.mouse.get_pos()[0]
            ke=drag_e-drag_s
            ks=drag_s-drag_e
            drag=True
            ball_dx=ks
        else:
          pass
    time=(pygame.time.get_ticks()-start_time)/1000
    v=(9.8)*time
    if not click:
        ball_y+=v
        ball_x+=ball_dx/100
        if ball_y>900:
            ball_y=900
            start_time=pygame.time.get_ticks()
            v=0
            ball_dx=0
        ks,ke=0,0
    else:
      v=0
      if drag_s<drag_e:
        pygame.draw.rect(screen,(255,0,0),(drag_s,ball_y-2,ke,4),0)
      else:
        pygame.draw.rect(screen,(255,0,0),(drag_e,ball_y-2,ks,4),0)
    text=font.render("v = "+str(round(math.sqrt(v**2+(ball_dx/100)**2),3)),True,(255,255,255))
    pygame.draw.circle(screen,(200,200,200),[ball_x,ball_y],size,0)
    screen.blit(text,(10,10))
    pygame.display.flip()
pygame.quit()