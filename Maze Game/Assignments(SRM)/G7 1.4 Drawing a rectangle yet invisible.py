#Task 1: Run the program and check if you can see the rectangle in the game screen
#Task 2: Observe the code of rectangle and window fill color -
#Task 3: check the line numbers of the codes and try to make it visible

import pygame
pygame.init()
pygame.display.set_caption("My First Game")
window = pygame.display.set_mode((600, 400))
white = (255, 255, 255)

while True:

  pygame.draw.rect(window, (255, 255, 0), (100, 100, 50, 50)) #(window, color, (x, y, width, height))

  window.fill(white)
  pygame.display.flip()
