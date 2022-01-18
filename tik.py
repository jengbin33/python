# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 21:12:24 2021

@author: jengbin
"""
import math
import pygame as pg
# 상수들
WIDTH = 550
ROW = 3
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (200,200,200)
RED = (255,0,0)
BLUE = (0,0,255)
pg.init()
win = pg.display.set_mode((WIDTH,WIDTH))
pg.display.set_caption("틱택톡")
X_IMAGE = pg.transform.scale(pg.image.load("C:\\Users\\jengbin\\Downloads\\x.png"), (150, 150))
O_IMAGE = pg.transform.scale(pg.image.load("C:\\Users\\jengbin\\Downloads\\o.png"), (150, 150))
END_FONT = pg.font.SysFont("courier", 40)
def grid():
    dis_to_center = WIDTH//ROW//2
    game_array = [[None,None,None],[None,None,None],[None,None,None]]
    for i in range(len(game_array)):
        for j in range(len(game_array)):
            x = dis_to_center*(2*j+1)
            y = dis_to_center*(2*i+1)
            game_array[i][j] = (x,y,"",True)
    return game_array
def draw_grid():
    gap = WIDTH//ROW 
    x = 0
    for i in range(ROW):
        x = i*gap
        pg.draw.line(win,GRAY,(x,0),(x,WIDTH),3)
        pg.draw.line(win,GRAY,(0,x),(WIDTH,x),3) 
    
def reset_win():
    win.fill(WHITE)
    draw_grid() 
    for image in images:
        x,y,IMAGE = image
        win.blit(IMAGE,(x-IMAGE.get_width()//2,y-IMAGE.get_height()//2))
    pg.display.update()
     
def click(game_array):
    global x_turn, o_turn, images
    m_x,m_y = pg.mouse.get_pos()
    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x,y,p,can_play = game_array[i][j]
            dis = math.sqrt((x-m_x)**2+(y-m_y)**2)
            if dis<WIDTH//ROW//2 and can_play:
                if x_turn:
                    images.append((x,y,X_IMAGE))
                    game_array[i][j] = (x,y,"x",False)
                    x_turn = False
                    o_turn = True
                elif o_turn:
                    images.append((x,y,O_IMAGE))
                    game_array[i][j] = (x,y,"o",False)
                    x_turn = True
                    o_turn = False
def has_won(game_array):
    for row in range(len(game_array)):
        if (game_array[row][0][2] == game_array[row][1][2] == game_array[row][2][2]) and game_array[row][0][2] != "":
            display_message(game_array[row][0][2].upper()+" has won.")
            return True
    for col in range(len(game_array)):
        if (game_array[0][col][2] == game_array[1][col][2] == game_array[2][col][2]) and game_array[0][col][2] != "":
            display_message(game_array[0][col][2].upper()+" has won.")
            return True
    if (game_array[0][0][2] == game_array[1][1][2] == game_array[2][2][2]) and game_array[0][0][2] != "":
        display_message(game_array[0][0][2].upper()+" has won.")
        return True
    if (game_array[0][2][2] == game_array[1][1][2] == game_array[2][0][2]) and game_array[0][2][2] != "":
        display_message(game_array[0][2][2].upper()+" has won.")
        return True
    return False
def has_drawn(game_array):
    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            if game_array[i][j][2] == "":
                return False
    display_message("IT's draw")
    return False
def display_message(message):
    pg.time.delay(500)
    win.fill(WHITE)
    text = END_FONT.render(message,1,BLACK)
    win.blit(text,((WIDTH-text.get_width())//2,(WIDTH-text.get_height())//2))
    pg.display.update()
    pg.time.delay(3000)
def main():
    global x_turn,o_turn,images,draw
    images = []
    draw = False 
    run = True   
    x_turn = True
    o_turn = False
    game_array = grid()
    
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                click(game_array)
        reset_win()
        if has_won(game_array) or has_drawn(game_array):
            run = False
while True:
        
    if __name__ == "__main__":
        main()
    
    
    