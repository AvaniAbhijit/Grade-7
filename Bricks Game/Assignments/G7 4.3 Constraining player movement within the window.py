#Task 1: Run the game and move the paddle to extreme right. Also, then move the paddle towards left.
#Task 2: Restrict the movement of paddle on the left.

import pygame

WIDTH, HEIGHT = 800, 600
BLUE = (0, 0, 255)

paddle_width = 100
paddle_height = 20
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - paddle_height - 20
paddle_speed = 10

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Brick Game')

while True:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()

  # Player movement
  keys = pygame.key.get_pressed()
  if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
    paddle_x += paddle_speed
  if keys[pygame.K_LEFT]:
    paddle_x -= paddle_speed

  window.fill((255,255,255))
  pygame.draw.rect(window, BLUE, [paddle_x, paddle_y, paddle_width, paddle_height])
  pygame.display.update()

  pygame.time.Clock().tick(60)
