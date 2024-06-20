# Task - Add another obstacle at coordinates (450, 420) having a width of 30 pixels and a height of 200 pixels.

import pygame

green = (0, 255, 0)
brown = (110, 38, 14) #defining brown color using rgb values

window_width, window_height = 500, 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Maze')

player_x, player_y = 0, 450
player_speed = 1

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()

  keys = pygame.key.get_pressed()
  if keys[pygame.K_RIGHT]:
    player_x += player_speed
  if keys[pygame.K_LEFT]:
    player_x -= player_speed
  if keys[pygame.K_UP]:
    player_y -= player_speed
  if keys[pygame.K_DOWN]:
    player_y += player_speed

  window.fill((255, 255, 255))
  player=pygame.draw.rect(window, green, (player_x, player_y, 50, 50))
  pygame.draw.rect(window, brown, (0, 0, 400, 50))  #adding first obstacle
  pygame.display.update()
  pygame.time.Clock().tick(60)
