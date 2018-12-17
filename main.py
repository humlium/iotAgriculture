#import 
import sys, random, math, datetime
import pygame, pygame.gfxdraw
from pygame.locals import *

#display define
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 480
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
BTN_HOME_ORI_X = 720
BTN_HOME_ORI_Y = 70
BTN_MANUAL_ORI_X = 720
BTN_MANUAL_ORI_Y = 170
HOUR_CENTER = (147, 343)
MIN_CENTER = (402, 343)
HOUR_REC_DETECT = (26, 257, 221, 458)   #(x min, x max, y min, y max)
MIN_REC_DETECT = (294, 511, 221, 458) #(x min, x max, y min, y max)
FPS = 30
MAIN_PAGE  = 1
MANUAL_PAGE = 2

#color define
WHITE  = (255, 255, 255)

pygame.init()
pygame.font.init()

comic20 = pygame.font.SysFont('Comic Sans MS', 20)
tvTest = comic20.render('10:10', False, WHITE)
tvMin = comic20.render('0', False, WHITE)
tvHour = comic20.render('0', False, WHITE)
screen = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption('iot Agriculture')

imgHome = pygame.image.load('mainUI.png')
imgManual = pygame.image.load('manualUI.png')
imgBtnHome = pygame.image.load('btnHome.png')
imgBtnManual = pygame.image.load('btnManual.png')

clock = pygame.time.Clock()

def findAng(x, y, x_cen, y_cen, kind):
        dis_x = x - x_cen
        dis_y = y - y_cen
        rad = math.atan2(dis_y, dis_x)
        ang = math.degrees(rad)+90
        if ang >= 0:
                if kind == 'MIN':
                        return round(ang/6)
                else :
                        return round(ang/15)
        if ang < 0 :
                ang = math.degrees(rad)+180
                if kind == 'MIN':                        
                        return round((ang/6)+45)
                else :
                        return round((ang/15)+18)
        
                

def main():      
        global tvMin, tvHour
        page = 1
        while True:       
                for event in pygame.event.get():
                        if event.type == QUIT:
                                pygame.quit()
                                sys.exit()  
                        if event.type ==  pygame.MOUSEBUTTONUP:
                                x, y = event.pos  
                                print('point',x, y)
                                if page == MANUAL_PAGE:
                                        if x > MIN_REC_DETECT[0] and x < MIN_REC_DETECT[1] and y > MIN_REC_DETECT[2] and y < MIN_REC_DETECT[3]:
                                                ang = findAng(x, y, MIN_CENTER[0], MIN_CENTER[1], 'MIN')
                                                tvMin = comic20.render(str(ang), False, WHITE)
                                        if x > HOUR_REC_DETECT[0] and x < HOUR_REC_DETECT[1] and y > HOUR_REC_DETECT[2] and y < HOUR_REC_DETECT[3]:
                                                ang = findAng(x, y, HOUR_CENTER[0], HOUR_CENTER[1], 'HOUR')
                                                tvHour = comic20.render(str(ang), False, WHITE)
                                                
                                #dis_x = x - 156
                                #dis_y = y - 311
                                #print(dis_x, dis_y)
                                #rad = math.atan2(dis_y, dis_x)
                                #ang = math.degrees(rad)+90  
                                #print(ang) 
                                #if(ang>=0):
                                #        print((ang/6)) 
                                #if(ang<0):
                                #        ang2 = math.degrees(rad)+180
                                #        print((ang2/6)+45)
                                if pygame.Rect(BTN_HOME_ORI_X, BTN_HOME_ORI_Y, imgBtnHome.get_width(), imgBtnHome.get_height()).collidepoint(x,y):
                                        page = MAIN_PAGE
                                        print(x, y) 
                                if pygame.Rect(BTN_MANUAL_ORI_X, BTN_MANUAL_ORI_Y, imgBtnManual.get_width(), imgBtnManual.get_height()).collidepoint(x,y):
                                        page = MANUAL_PAGE
                if page == MAIN_PAGE:
                        screen.blit(imgHome, (0, 0))
                else :
                        screen.blit(imgManual, (0, 0))
                        screen.blit(tvMin, MIN_CENTER)
                        screen.blit(tvHour, HOUR_CENTER)
                screen.blit(imgBtnHome, (BTN_HOME_ORI_X, BTN_HOME_ORI_Y))
                screen.blit(imgBtnManual, (BTN_MANUAL_ORI_X, BTN_MANUAL_ORI_Y))
                screen.blit(tvTest, (10, 10))
                pygame.display.update()
                clock.tick(FPS)

if __name__=='__main__':
        main()