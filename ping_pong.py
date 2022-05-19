from pygame import *
from random import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size1, size2, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size1, size2))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.x < 620:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.x < 620:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 700:
            self.rect.x = randint(80, 420)
            self.rect.y = 0
            lost += 1

class Ball(GameSprite):
    def update(self):
        if
#окно
window = display.set_mode((700, 500))
display.set_caption('Galaxy(шутер)')
#картинка
background = transform.scale(image.load('fon.jpg'), (700, 500))
#спрайт
player1 = Player('player.jpg', 50, 230, 65, 65, 5)
player2 = Player('player.jpg', 570, 230, 65, 65, 5)
boll = GameSprite('player.jpg', 325, 230, 65, 65, 5)
#ширифт
font = font.Font(None, 35)

#частота кадров
FPS = 50
clock = time.Clock()

speed_x = 3
speed_y = 3

run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.blit(background, (0,0))

    player1.reset()
    player1.update()

    player2.reset()
    player2.update2()

    boll.reset()
    boll.rect.x += speed_x
    boll.rect.y += speed_y
    if boll.rect.y < 0 or boll.rect.y > 500:
        speed_y *= -1
    if sprite.collide_rect(player1, boll) or sprite.collide_rect(player2, boll):
        speed_x *= -1

    display.update()
    clock.tick(FPS)