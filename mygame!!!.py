import pygame

# screen size 
WINDOW_W = 1336
WINDOW_H = 765
WINDOW_SIZE = (WINDOW_W, WINDOW_H)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("ziv - game ")

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


def print_lasers():
  for i in range(len(laser_list)):
    l = laser_list[i]
    screen.blit(laser_image,(l[0],l[1]))
    laser_list[i] = [l[0],l[1]-30]

  if len(laser_list) > 0 and laser_list[0][1] < 0:
    laser_list.remove(laser_list[0])




while play:
  screen.blit(bk_image,(0,0))
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
        laser_list.append([ship_x+21,ship_y])

  screen.blit(ship_image,(ship_x,ship_y))
  pygame.draw.circle(screen,(255,255,255),(circle_x , circle_y),10)
  print_lasers()

  circle_x +=circle_x_step
  if circle_x > WINDOW_W:
    circle_x_step = -10
  if circle_x <0 :
    circle_x_step = 10
  
  pygame.display.flip()


  clock.tick(10)

pygame.quit()
