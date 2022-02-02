from random import random
from turtle import delay
import pygame
import time
import pygame.freetype
from pygame import mixer

# screen size 
WINDOW_W = 1336
WINDOW_H = 600
WINDOW_SIZE = (WINDOW_W, WINDOW_H)


pygame.init()
mixer.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
myfont = pygame.font.SysFont('Comic Sans MS', 30)
pygame.display.set_caption("ziv - game ")
background_music = pygame.mixer.Sound("mis.mp3")
pygame.mixer.music.load("mis.mp3")
pygame.mixer.Channel(1).play(background_music)

# www.pngaaa.com
bk_image = pygame.image.load("gameback.jpg")
ship_image = pygame.image.load("amo.png")
ship_image = pygame.transform.scale(ship_image, (50, 80)) 
laser_image = pygame.image.load("laser2.png")
laser_image = pygame.transform.scale(laser_image, (10, 20)) 
clock = pygame.time.Clock()

circle_x = 10
circle_y = WINDOW_H /2
ship_x = WINDOW_W /2
ship_y = WINDOW_H - 80

circle_x_step = 10
x_step = 10
laser_list = []
play = True

sc = 0
def print_lasers():
  global sc , circle_x
  for i in range(len(laser_list)):
    laser = laser_list[i]
    screen.blit(laser_image,(laser[0],laser[1]))
    laser_list[i] = [laser[0],laser[1]-30]
    if is_laser_hit(laser):
      print("hit")
      sc +=1
      circle_x = 0
def is_laser_hit(laser_pos):
  return abs(laser_pos[0]-circle_x) <30 and abs(laser_pos[1]-circle_y) <30 


while play:
  screen.blit(bk_image,(0,0))
  textsurface = myfont.render("score :"+str(sc), False, (255, 255, 255))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        ship_x -= x_step
      if event.key == pygame.K_RIGHT:
        ship_x += x_step
      if event.key == pygame.K_UP :
        ship_y -= 10
      if event.key == pygame.K_DOWN:
        ship_y += 10
      if event.key == pygame.K_SPACE:
        shot_sound = pygame.mixer.Sound("ero.mp3")
        pygame.mixer.music.load("ero.mp3")
        pygame.mixer.music.play()
        laser_list.append([ship_x+21,ship_y])
  screen.blit(ship_image,(ship_x,ship_y))
  pygame.draw.circle(screen,(255,255,255),(circle_x , circle_y),10)
  print_lasers()
  screen.blit(textsurface,(0,0))
  circle_x +=circle_x_step
  if circle_x > WINDOW_W:
    circle_x_step = -10
  if circle_x <0 :
    circle_x_step = 10
  
  pygame.display.flip()


  clock.tick(10)
pygame.quit()
