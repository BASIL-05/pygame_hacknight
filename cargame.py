import pygame
from pygame.locals import *
import random

size=width,height=(1200,800)
road_width = int (width/1.6)
roadmark_width=int(width/80) 
right_lane =width/2+road_width/4
left_lane=width/2-road_width/4
speed=1
pygame.init()
running =True
screen= pygame.display.set_mode((size))
pygame.display.set_caption("Thomman's kali 😌")
screen.fill((240,248,255))

pygame.display.update()
car=pygame.image.load("car.png")
car_loc=car.get_rect()
car_loc.center=right_lane,height*0.8

car2=pygame.image.load("othercar.png")
car2_loc=car2.get_rect()
car2_loc.center=left_lane,height*0.2
counter=0
while running:
    counter+=1
    if counter == 5000:
        speed+=0.15
        counter=0
        print("LEVELLING UP!!",speed)
    car2_loc[1]+=speed
    if car2_loc[1] >height:
       
        if random.randint(0,1)==0:
            car2_loc.center=right_lane,-200
        else:
            car2_loc.center=left_lane,-200
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1]-250:
        print("GAME IS OVER !!!!")
        break
        
    for event in pygame.event.get():
        if event.type ==QUIT:
            running=False
        if event.type ==KEYDOWN:
            if event.key in[K_a,K_LEFT]
                car_loc=car_loc.move([- int(road_width/2),0])
            if event.key in[K_d,K_RIGHT]:
                car_loc=car_loc.move([int(road_width/2),0])
    car=pygame.image.load("car.png")
car_loc=car.get_rect()
car_loc.center=width/2 + road_width/4,height+0.8  
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
    screen.blit(car,car_loc)
    screen.blit(car2,car2_loc)
    pygame.display.update()

pygame.quit()
