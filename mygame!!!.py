import pygame

WINDOW_W = 768
WINDOW_H = 1366
IMAGE = 'gameback.jpg'
pygame.init()
size = (WINDOW_H , WINDOW_W)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mitko")
img = pygame.image.load(IMAGE)
clock = pygame.time.Clock()
circle_x = 10
circle_y = WINDOW_W / 2
add = 10
finish = False

# main loop

while not finish :
  screen.blit(img, (0,0))
  pygame.draw.circle(screen,(255,255,255),[circle_x,circle_y],10)
  circle_x += 10
  if circle_x > WINDOW_H :
    add = -10
  if circle_x < 0 :
    add = 10
 
      
  pygame.display.flip()
  for event in pygame.event.get():
    if event.type ==pygame.QUIT:
      finish = True
  clock.tick(20)
  
pygame.quit()
