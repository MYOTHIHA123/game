import sys

import pygame as pg
print(sys.path)

pg.init()

screen_width = 800
screen_height = 600

display = pg.display.set_mode((screen_width,screen_height))

pg.display.set_caption('космическое вторжение')
#icon_img = pg.image.load('resources/img/ufo.png')
#pg.display.set_icon(icon_img)


background_img = pg.image.load('resources/img/background.png')
display.blit(background_img, (0,0))

sysfont = pg.font.SysFont('arial', 50)
text_img = sysfont.render(' myo thiha kyaw', True, 'red')
#display.blit(text_img, (380, 500))
w = text_img.get_width()
h = text_img.get_height()
#font = pg.font.Font('resources/font/04B_19__.TTF', 48)
#game_over_img = font.render('Game Over', True, 'white')
#w = game_over_img.get_width()
#h = game_over_img.get_height()
x = screen_width - w
y = screen_height - h
#display.blit(game_over_img, (x, y))
running = True
while running:
    #display.fill('blue',(20, 50, 100, 250))
    #display.blit(text_img, (x, y))
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN and event.key == pg.K_q:
            running = False
        if event.type == pg.KEYUP and event.key == pg.K_m:
            print('Press m')
            display.blit(text_img, (x, y))
        if event.type == pg.KEYUP and event.key == pg.K_z:
            print('Press z')





pg.quit()