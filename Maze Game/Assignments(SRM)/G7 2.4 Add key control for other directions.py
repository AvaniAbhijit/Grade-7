#Task 1: Add key control for moving player left using the "LEFT" arrow key
#Task 2: Add key control for moving player up and down using "UP" and "DOWN" arrow keys

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

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
      player_x += 1


    window.fill((255, 255, 255))
    player=pygame.draw.rect(window, green, (player_x, player_y, 50, 50))
    pygame.display.update()
    pygame.time.Clock().tick(60)
