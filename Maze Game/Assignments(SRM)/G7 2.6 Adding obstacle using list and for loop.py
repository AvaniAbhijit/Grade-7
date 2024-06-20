#Task: Run the code and understand the use of list in line 14 to create rectangles using loop in line 39 and 40

import pygame

green = (0, 255, 0)
brown = (110, 38, 14)
blue = (0, 0, 255)

window_width, window_height = 500, 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Maze')

#Adding obstacles inside list
obstacles = [
    pygame.Rect(0, 0, 400, 50)
]

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

  for object in obstacles: #using a for loop to draw all the obstacles
    pygame.draw.rect(window, brown, object) #adding each obstacle on screen
  pygame.display.update()
  pygame.time.Clock().tick(60)
