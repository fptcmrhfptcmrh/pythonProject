import pygame
import random

pygame.init()
dis = pygame.display.set_mode((1000, 900))
pygame.display.update()
pygame.display.set_caption('typical Snake game')
purple = (255, 0, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
x1 = 300
y1 = 300
x1_change = 0
y1_change = 0
clock = pygame.time.Clock()
snake_speed=15
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, blue)
    dis.blit(value, [0, 0])
def our_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, purple, [x[0], x[1], 10, 10])
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg,[200, 400])
def gameLoop():
    gameover = False
    game_close = False
    x1 = 490
    y1 = 440
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, 990) / 10.0) * 10.0
    foody = round(random.randrange(0, 890) / 10.0) * 10.0
    while not gameover:
        while game_close:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameover = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0
        if x1>=1000 or x1<0 or y1>=900 or y1<0:
             game_close=True
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis, blue, [foodx, foody, 10, 10])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, 990) / 10.0) * 10.0
            foody = round(random.randrange(0, 890) / 10.0) * 10.0
            Length_of_snake += 500
        clock.tick(30)
    pygame.quit()
    quit()
gameLoop()
