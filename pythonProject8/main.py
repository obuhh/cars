import queue
import pygame
import random

pygame.init()
win = pygame.display.set_mode((1000, 200))
pygame.display.set_caption("CARS")
wp = [pygame.image.load('skin/wy.png'), pygame.image.load('skin/wb.png'), pygame.image.load('skin/wg.png'),
      pygame.image.load('skin/wl.png'), pygame.image.load('skin/ws.png'), pygame.image.load('skin/we.png')]
men = pygame.image.load('skin/menu10.png')

class Button:
    def __init__(self, x, y, w, h, unpr, pr, act, action, text):
        self.x = x
        self.y = y
        self.unpr = unpr
        self.pr = pr
        self.act = act
        self.h = h
        self.w = w
        self.action = action
        self.text = text

    def draw(self):
        pygame.draw.rect(win, self.unpr, (self.x, self.y, self.w, self.h))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x < mouse[0] < self.x + self.w:
            if self.y < mouse[1] < self.y + self.h:
                if click[0]:
                    pygame.draw.rect(win, self.pr, (self.x + 10, self.y + 10, self.w - 20, self.h - 20))
                    if self.action is not None:
                        self.action()
                else:
                    pygame.draw.rect(win, self.act, (self.x + 10, self.y + 10, self.w - 20, self.h - 20))
        print_text(self.text, self.x + 20, self.y + 10)

class Car():

    def __init__(self, pos = 0, speed = 0, maxspeed = 0, acceleration = 0):
        self.pos = pos
        self.speed = speed
        self.maxspeed = maxspeed
        self.acceleration = acceleration

    def draw(self):
        pygame.draw.rect(win, (255, 211, 155), (30.6, self.pos, 200, 100))
        #print(self.pos)
        #print_text(self.text, self.x + 20, self.y + 10)

b = []

acc1 = 0.003
acc2 = 0.08
c = 5
Cars = 50


def print_text(message, x, y, font_color=(0, 0, 0), font_size=30):
    # font_type = pygame.font.Font(font_type, font_size)
    font = pygame.font.SysFont('comicsansms', font_size)
    text = font.render(message, 1, font_color)
    win.blit(text, (x, y))

col = [(0, 255, 0), (255, 0, 0)]

def drawWindow():
    win.fill((0, 0, 0))
    for j in range(1, Cars):
        pygame.draw.rect(win, col[b[j][3]], (b[j][2], 30, 5, 5))


b = []
for i in range(Cars + 1):
    b.append([0] * 4)
k = 0
for i in range(0, Cars):
    b[i][0] = 0
    b[i][1] = 0.5
    b[i][2] = k * 10
    k = k + 1
b[Cars][0] = 0
b[Cars][2] = 15000
def set():
    k = 0
    for i in range(0, Cars):
        b[i][0] = 0
        b[i][1] = 0.5
        b[i][2] = k * 10
        b[i][3] = 0
        k = k + 1
    b[Cars][0] = 0
    b[Cars][2] = 15000

def recountMas():
    for i in range(0, Cars):
        if (abs(b[i + 1][2] - b[i][2]) < c):
            if (b[i][0] > 0):
                b[i][0]  = b[i][0] - acc2
            else:
                b[i][0]  = 0
            b[i][3] = 1
        else:
            if (b[i][0] < b[i][1]):
                b[i][0] = b[i][0] + acc1
            else:
                b[i][0] = b[i][1]
            b[i][3] = 0
        b[i][2] = b[i][2] + b[i][0]
        print(b[i][0],' ', c)

def recountMas2():
    i1 = random.randint(0, Cars)
    i2 = random.randint(0, Cars)
    for i in range(0, Cars):
        if (abs(b[i + 1][2] - b[i][2]) < c) or (i == i1) or (i == i2):
            if (b[i][0] > 0):
                b[i][0] = b[i][0] - acc2
            else:
                b[i][0] = 0
            b[i][3] = 1
        else:
            if (b[i][0] < b[i][1]):
                b[i][0] = b[i][0] + acc1
            else:
                b[i][0] = b[i][1]
            b[i][3] = 0
        b[i][2] = b[i][2] + b[i][0]
        print(b[i][0], ' ', c)

def menu():
    kek = True
    while kek:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            kek = False
        drawWindow()
        win.blit(men, (0, 0))
        pygame.display.update()


drawWindow()
menu()
run = True
fl = False
while run:
    pygame.time.delay(70)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        fl = False
        menu()
    if keys[pygame.K_n]:
        fl = True
    if keys[pygame.K_m]:
        fl = False
    if keys[pygame.K_r]:
        set()
    if keys[pygame.K_b]:
        recountMas2()
    if fl or keys[pygame.K_SPACE]:
        recountMas()
    drawWindow()
    pygame.display.update()
pygame.quit()
