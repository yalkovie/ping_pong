from pygame import *
from random import *
font.init()

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

#окно
window = display.set_mode((700, 500))
display.set_caption('Ping Pong')

#картинка
background = transform.scale(image.load('Fon.png'), (700, 500))

#спрайт
player1 = Player('Player.png', 50, 230, 25, 100, 5)
player2 = Player('Player.png', 570, 230, 25, 100, 5)
boll = GameSprite('Ball.png', 325, 230, 50, 50, 5)

#ширифт
font = font.SysFont("Arial", 40)
lose1 = font.render('Player 1 проиграл!', True, (180, 0, 0))
lose2 = font.render('Player 2 проиграл!', True, (180, 0, 0))

#частота кадров
FPS = 60
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
    '''
    if boll.rect.y < 0 or boll.rect.y > 450:
        speed_y *= -1
    if boll.rect.x < 0 or boll.rect.x > 650:
        speed_x *= -1
    '''
    if boll.rect.y < 0 or boll.rect.y > 450:
        speed_y *= -1
    if boll.rect.x < 0:
        window.blit(lose1, (200, 200))
    if boll.rect.x > 650:
        window.blit(lose2, (200, 200))
    if sprite.collide_rect(player1, boll) or sprite.collide_rect(player2, boll):
        speed_x *= -1

    display.update()
    clock.tick(FPS)
