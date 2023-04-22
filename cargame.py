import pygame
from pygame.locals import *

size=width,height=(1200,800)
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
car=pygame.image.load("car.png")
car_loc=car.get_rect()
car_loc.center=width/2 + road_width/4,height*0.8

car2=pygame.image.load("othercar.png")
car2_loc=car2.get_rect()
ca2r_loc.center=width/2 - road_width/4,height+0.8
while running:
    for event in pygame.event.get():
        if event.type ==QUIT:
            running=False
        if event.type ==KEYDOWN:
            if event.key in[K_a,K_LEFT]
                car_loc=car_loc.move([- int(road_width
            
    screen.blit(car,car_loc)
    pygame.display.update()

pygame.quit()
