import pygame

WINDOW_W = 768
WINDOW_H = 1366
IMAGE = 'ima.jpg'
pygame.init()
size = (WINDOW_H , WINDOW_W)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("GTA V")
img = pygame.image.load(IMAGE)

y = 0
x = 0
finish = False
while not finish :
  screen.blit(img, (0,0))
  
#   for i in range (10):
  for i in range (0,600,50):
      y += 50
      pygame.draw.line(screen,(255,255,255),[0,0],[600,i],8)
  pygame.display.flip()
#   for i in range (10):
#       x += 50
#       pygame.draw.line(screen,(0,255,100),(x,0),(x,432))
  for event in pygame.event.get():
    if event.type ==pygame.QUIT:
      finish = True
  
pygame.quit()
