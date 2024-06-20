#Skip this program and move to next

import pygame
green = (0, 255, 0)
window_width, window_height = 500, 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Maze')

player_x, player_y = 0, 450

while True:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()
  window.fill((255,255,255))
  player=pygame.draw.rect(window, green, (player_x,player_y,50,50))
  pygame.display.update()
