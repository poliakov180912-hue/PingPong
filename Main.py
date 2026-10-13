import sys
import pygame
import os

def resource_path(relative_path):
    """Получает абсолютный путь к ресурсам, работает для dev и для PyInstaller"""
    try:
        # PyInstaller создает временную папку в _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')

    return os.path.join(base_path, relative_path)


pygame.init()

SCREEN_W = 800
SCREEN_H = 500

window = pygame.display.set_mode((SCREEN_W, SCREEN_H))

background = pygame.image.load(resource_path('assets/pingpong.jpg'))
background = pygame.transform.scale(background, (SCREEN_W,SCREEN_H))

clock = pygame.time.Clock()

class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, filename, width, height, x=0, y=0, speed=5):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(resource_path(filename)), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = speed
        self.speed_y = speed
        self.strt_pos = (x,y)


    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def draw_hitbox(self):
        pygame.draw.rect(window, (255,0,0),self.rect)

class Platform(BaseSprite):
    def update_platform1(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed_y
        if keys[pygame.K_s] and self.rect.y <= 350:
            self.rect.y += self.speed_y

    def update_platform2(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed_y
        if keys[pygame.K_DOWN] and self.rect.y <= 350:
            self.rect.y += self.speed_y

class Ball(BaseSprite):
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x <= 0 or self.rect.x >= 730:
            self.speed_x *= -1
        if self.rect.y <= -15 or self.rect.y >= 430:
            self.speed_y *= -1



ball = Ball('assets/ball.png', 70,70,400,200, 7)
stick1 = Platform('assets/stick.png', 20,150, 50,150)
stick2 = Platform('assets/stick.png', 20,150, 720,150)
platforms = pygame.sprite.Group(stick1, stick2) # noqa
while True:
    clock.tick(40)
    window.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    ball.update()
    ball.draw()
    '''stick1.draw_hitbox()
    stick2.draw_hitbox()'''
    stick1.update_platform1()
    stick1.draw()
    stick2.update_platform2()
    stick2.draw()
    collided = pygame.sprite.spritecollide(ball,platforms, False) # noqa
    if collided:
        ball.speed_x *= -1
        ball.speed_y *= -1
    if ball.rect.x <= 0 or ball.rect.x >= 730:
        break

    pygame.display.update()

while True:
    clock.tick(40)
    window.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()