#Task: Create 4 more rectangular regions with below details in the "obstacles" list
# Rect3: Coordinates(200,150), width = 400 and height = 50
# Rect4: Coordinates(60,280), width = 150 and height = 50
# Rect5: Coordinates(180.350), width = 200 and height = 50
# Rect6: Coordinates(450,420), width = 30 and height = 200

import pygame

green = (0, 255, 0)
brown = (110, 38, 14)
blue = (0, 0, 255)

window_width, window_height = 500, 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Maze')

#Adding obstacles inside list
obstacles = [
    pygame.Rect(0, 0, 400, 50),
    pygame.Rect(60, 90, 50, 200),




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

  for object in obstacles:
    pygame.draw.rect(window, brown, object)

  # win= pygame.draw.rect(window, blue,(450, 0, 70, 70))

  pygame.display.update()
  pygame.time.Clock().tick(60)
