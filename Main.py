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
        self.speed = speed
        self.strt_pos = (x,y)

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def draw_hitbox(self):
        pygame.draw.rect(window, (255,0,0),self.rect)

ball = BaseSprite('assets/ball.png', 80,80,400,200)
stick = BaseSprite('assets/stick.png', 150,150, 50,150)

while True:
    clock.tick(40)
    window.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    ball.draw()
    stick.draw()



    pygame.display.update()