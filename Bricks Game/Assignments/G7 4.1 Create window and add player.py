#Task - Change paddle width, height and division values
# and run the  program to observe the changes.

import pygame

WIDTH, HEIGHT = 800, 600
BLUE = (0, 0, 255)

# Paddle
paddle_width = 100
paddle_height = 20
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - paddle_height - 20

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Brick Game')

while True:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()
  window.fill((255,255,255))

  pygame.draw.rect(window, BLUE, [paddle_x, paddle_y, paddle_width, paddle_height])
  pygame.display.update()
