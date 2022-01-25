import pygame
import random
import myBD
from datetime import datetime

WIDTH = 1920
HEIGHT = 1080
FPS = 60

bd = myBD.myBDS()
bd.create_bd()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

scet = 0
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("InSpace")
clock = pygame.time.Clock()
score = 0


class InSpace(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((70, 70))
        self.radius = 25
        self.image = pygame.transform.scale(ship, (70, 70))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.lives = 3
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 100
        self.speedx = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystat = pygame.key.get_pressed()

        if keystat[pygame.K_a]:
            self.speedx = -8
        if keystat[pygame.K_d]:
            self.speedx = 8
        if keystat[pygame.K_w]:
            self.speedy = -8
        if keystat[pygame.K_s]:
            self.speedy = 8

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.x > WIDTH:
            self.rect.x = 0
        if self.rect.x < 0:
            self.rect.x = WIDTH

        if self.rect.y > HEIGHT:
            self.rect.y = 0
        if self.rect.y < 0:
            self.rect.y = HEIGHT

    def fire(self):
        bullet = Potron(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Meteorits(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(meteorit, (40, 40))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-80, -40)
        self.speedy = random.randrange(5, 10)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -40 or self.rect.right > WIDTH + 40:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-80, -40)
            self.speedy = random.randrange(5, 10)


class Potron(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image = laser
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
        shootM.play()

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(background_image)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

font_name = pygame.font.match_font('arial')

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x - 50 * i
        img_rect.y = y
        surf.blit(pygame.transform.scale(chlive, (35, 35)), img_rect)


def show_go_screen():
    screen.blit(background_image, background_rect)
    scet = score
    try:
        bd = myBD.myBDS()
        nowdata = datetime.now()
        bd.add_item(str(nowdata.day) + '.' + str(nowdata.month) + '.' + str(nowdata.year) + ' - время ' + str(
            nowdata.hour) + ':' + str(nowdata.minute), score)
    except BaseException:
        f = open('logF.txt', 'a')
        f.write('Ошибка в Window obnL' + '\n')

    draw_text(screen, "InSpace", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Ваш счет " + str(scet), 32, WIDTH / 2, HEIGHT * 1.5 / 4)
    draw_text(screen, "W-Вперед,S-назад,A-вправо,D-влево", 32, WIDTH / 2, HEIGHT * 2 / 4)
    draw_text(screen, "Правая кнопка мышки-стрелять", 32, WIDTH / 2, HEIGHT * 2.5 / 4)
    draw_text(screen, "Нажмите левую кнопку мыши что бы начать!", 18, WIDTH / 2, HEIGHT * 3 / 4)

    h = []
    try:
        bd = myBD.myBDS()
        bd.create_bd()
        h = bd.get_allitem()
    except BaseException:
        f = open('logF.txt', 'b')
        f.write('Ошибка в Window obnL' + '\n')

    draw_text(screen, "Ваши 3 последних результата", 20, WIDTH - 1700, HEIGHT / 4)
    draw_text(screen, "Дата: " + str(h[len(h) - 1][0]) + ' Очки: ' + str(h[len(h) - 1][1]), 20, WIDTH - 1700,
              HEIGHT * 1.2 / 4)
    draw_text(screen, "Дата: " + str(h[len(h) - 2][0]) + ' Очки: ' + str(h[len(h) - 2][1]), 20, WIDTH - 1700,
              HEIGHT * 1.4 / 4)
    draw_text(screen, "Дата: " + str(h[len(h) - 3][0]) + ' Очки: ' + str(h[len(h) - 3][1]), 20, WIDTH - 1700,
              HEIGHT * 1.6 / 4)

    draw_text(screen, "Для уровня сложности лекго во время игры нажмите на 1", 20, WIDTH - 1600,
              HEIGHT * 2 / 4)
    draw_text(screen, "Для уровня сложности средне во время игры нажмите на 2", 20, WIDTH - 1600,
              HEIGHT * 2.2 / 4)
    draw_text(screen, "Для уровня сложности невозможно во время игры нажмите на 3", 20, WIDTH - 1600,
              HEIGHT * 2.4 / 4)

    pygame.display.flip()

    kool = True
    while kool:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                kool = False


background_image = pygame.image.load('cosmos.jpg').convert()
ship = pygame.image.load('ship.png').convert()
laser = pygame.image.load('laser.png').convert()
meteorit = pygame.image.load('meteorit.png').convert()
chlive = pygame.image.load('chlive.png').convert()

shootM = pygame.mixer.Sound('LaserM.ogg')
boom = pygame.mixer.Sound('boom.ogg')
fon = pygame.mixer.Sound('fon.mp3')

all_sprites = pygame.sprite.Group()
meteor = pygame.sprite.Group()
StarShip = InSpace()
bullets = pygame.sprite.Group()
all_sprites.add(StarShip)

background_rect = background_image.get_rect()

for i in range(20):
    m = Meteorits()
    all_sprites.add(m)
    meteor.add(m)
fon.play(loops=-1)

game_over = True
running = True

show_go_screen()
while running:

    keystat = pygame.key.get_pressed()
    if keystat[pygame.K_1]:
        FPS = 60
        m = Meteorits()
        m.speedy = random.randrange(5, 10)
        m.speedy = random.randrange(-3, 3)

    keystat = pygame.key.get_pressed()
    if keystat[pygame.K_2]:
        FPS = 120
        m.speedy = random.randrange(10, 20)
        m.speedy = random.randrange(-5, 5)

    keystat = pygame.key.get_pressed()
    if keystat[pygame.K_3]:
        FPS = 240
        m.speedy = random.randrange(20, 30)
        m.speedy = random.randrange(-10, 10)

    keystat = pygame.key.get_pressed()
    if keystat[pygame.K_0]:
        FPS = 60
        StarShip.lives = -1

    screen.blit(background_image, (0, 0))
    clock.tick(FPS)
    if game_over == False:
        StarShip.lives = 3
        show_go_screen()
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        powerups = pygame.sprite.Group()
        StarShip = InSpace()
        all_sprites.add(StarShip)
        for i in range(20):
            m = Meteorits()
            all_sprites.add(m)
            meteor.add(m)
        scet = score
        score = 0
        game_over = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            StarShip.fire()

    all_sprites.update()

    hits = pygame.sprite.groupcollide(meteor, bullets, True, True)

    for hit in hits:
        m = Meteorits()
        all_sprites.add(m)
        meteor.add(m)
        boom.play()
        score += 1

    if StarShip.lives == 0:
        game_over = False

    hits = pygame.sprite.spritecollide(StarShip, meteor, True, pygame.sprite.collide_circle)
    if hits:
        StarShip.lives -= 1

    all_sprites.update()

    screen.blit(background_image, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, str(score), 40, WIDTH / 2, 10)
    draw_lives(screen, WIDTH - 100, 5, StarShip.lives,
               chlive)
    pygame.display.flip()
