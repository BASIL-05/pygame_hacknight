import pygame
from pygame.locals import *

size=width,height=(800,800)
road_width = int (width/1.6)
roadmark_width=int(width/80) 
pygame.init()
running =True
screen= pygame.display.set_mode((size))
pygame.display.set_caption("Thomman's kali 😌")
screen.fill((240,248,255))
pygame.draw.rect(
    screen,(50,50,50),(width/2-road_width/2,0,road_width,height)
)
pygame.draw.rect(
    screen,(238,59,59),(width/2-roadmark_width/2,0,roadmark_width,height)
)
pygame.draw.rect(
    screen,(255,240,60),(width/2-road_width/2+ roadmark_width*2,0,roadmark_width,height)
)
pygame.draw.rect(
    screen,(255,240,60),(width/2+road_width/2- roadmark_width*3,0,roadmark_width,height)
)
pygame.display.update()
while running:
    for event in pygame.event.get():
        if event.type ==QUIT:
            running=False

pygame.quit()