#Task 1: Play the game and move the block to right using key
#Task 2: Make player speed to increase by 5 every time the right key is pressed

import pygame

green = (0, 255, 0)
window_width, window_height = 500, 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Maze')

player_x, player_y = 0, 450
player_speed = 1

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()

  keys = pygame.key.get_pressed()  #storing the key pressed by user.
  if keys[pygame.K_RIGHT]:  #checking if right arrow is pressed
    player_x += 1  #increasing the x position of player by 1

  window.fill((255, 255, 255))
  player=pygame.draw.rect(window, green, (player_x, player_y, 50, 50))
  pygame.display.update()
  pygame.time.Clock().tick(60)
