import pygame
import random


white=(255, 255, 255)
black=(0, 0, 0)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(820, 900),
                random.randint(0, 600),
            )
        )
        self.speed = random.randint(5, 20)
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
clock = pygame.time.Clock()
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("cloud.png").convert()

        self.surf.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(820,900),
                random.randint(0, 600),
            )
        )
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-1, 5)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 600:
            self.rect.bottom = 600
pygame.init()

img_scale = (pygame.transform.scale(pygame.image.load("cloud.png"), (100, 100)))
pygame.image.save(img_scale, "cloud.png")
img_scale = (pygame.transform.scale(pygame.image.load("jet.png"), (50, 50)))
pygame.image.save(img_scale, "jet.png")


img_scale = (pygame.transform.scale(pygame.image.load("missile.png"), (100, 100)))
pygame.image.save(img_scale, "missile.png")

screen=pygame.display.set_mode((800,600))
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)
player=Player()
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
        elif event.type == pygame.QUIT:
            running = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type == ADDCLOUD:
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemies.update()
    clouds.update()
    screen.fill(black)
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    screen.blit(player.surf, player.rect)
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        running = False
    pygame.display.flip()
    clock.tick(30)
