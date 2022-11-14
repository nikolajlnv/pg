import pygame as pg

pg.init()
screen = pg.display.set_mode((720, 480))

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
