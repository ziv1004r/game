import pygame

WINDOW_H = 768
WINDOW_W = 1366
IMAGE = 'gameback.jpg'
pygame.init()
size = (WINDOW_W , WINDOW_H)
screen = pygame.display.set_mode(size)
png = pygame.image.load(r"C:\Users\pc\game\amo.png")
png = pygame.transform.scale(png,(50,80))
shot = 'shot.png.png'
shot = pygame.transform.scale(png,(40,60))
pygame.display.set_caption("Mitko ")
img = pygame.image.load(IMAGE)
clock = pygame.time.Clock()
circle_x = 10
circle_y = WINDOW_H / 2
add = 10
ship_x = WINDOW_W / 2
ship_y = WINDOW_H -80
finish = False



while not finish :
  screen.blit(img, (0,0))
  screen.blit(png, (ship_x,ship_y))
  # screen.blit(png, (ship_x,20))
  pygame.draw.circle(screen,(255,255,255),[circle_x,circle_y],10)
  circle_x += 10
  if circle_x > WINDOW_W :
    add = -10
  elif circle_x < 0 :
    add = 10
  
  x_s = ship_x
  y_s = ship_y
  for event in pygame.event.get():
    if event.type ==pygame.QUIT:
      finish = True
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        ship_x -= 10
      if event.key == pygame.K_RIGHT:
        ship_x += 10 
      if event.key == pygame.K_UP:
        ship_y -= 10
      if event.key == pygame.K_DOWN:
        ship_y += 10 
      if event.key == pygame.K_SPACE:
        for i in range (10):
          screen.blit(shot, (x_s,y_s))
          y_s -= 10
  pygame.display.flip()
  clock.tick(20)
  
pygame.quit()
