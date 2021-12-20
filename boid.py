import pygame as pg
import math
from random import *

class boid:
    def __init__(self, pos, angle, acceleration):
        self.pos = pos
        self.ang = angle
        self.a = acceleration
        self.t = 1
        self.vy = math.sin(self.ang)
        self.vx = math.cos(self.ang)

    def run(self, surf):
        self.vx = self.vx + self.a[0] * self.t
        self.vy = self.vy + self.a[0] * self.t
        self.pos[0] = self.pos[0] + self.vx * self.t
        self.pos[1] = self.pos[1] + self.vy * self.t
        if self.pos[0] > 1280:
            self.pos[0] -= 1280
        if self.pos[1] > 720:
            self.pos[1] -= 720
        if self.pos[0] < 0:
            self.pos[0] = 1
        if self.pos[1] < 0:
            self.pos[1] = 1
        draw_boid(surf, self.pos, self.ang)

def draw_boid(sc, pos, angle):

    pg.draw.circle(sc, "black", pos, 2)

    xpos = pos[0] + 10*math.cos(angle), pos[1] + 10*math.sin(angle)

    pg.draw.line(sc, "black", pos, xpos, 2)

size = width, height = 1280, 720

screen = pg.display.set_mode(size)
clock = pg.time.Clock()

bxy = [100, 200]
bang = math.pi / 4

bb = []

bxy = [randint(100,500), randint(100,500)]
bb.append(boid(bxy, math.pi / 4, [1/2]))

bb.append(boid(bxy, math.pi / 2, [1/2]))

while True:
    screen.fill("white")

    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    for i in range(import pygame as pg
import math
from random import *


def draw_boid(sc, pos, angle):
    pg.draw.circle(sc, "black", pos, 5)
    xpos = pos[0] + 10*math.cos(angle), pos[1] + 10*math.sin(angle)
    pg.draw.line(sc, "black", pos, xpos, 2)


size = width, height = 1280, 720

screen = pg.display.set_mode(size)
clock = pg.time.Clock()

bxy = bx, by = 100, 200
bang = 0

while True:
    screen.fill("white")

    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    draw_boid(screen, bxy, bang)

    pg.display.flip()
    clock.tick()):
        b.run(screen)

    pg.display.flip()
    clock.tick(10)
