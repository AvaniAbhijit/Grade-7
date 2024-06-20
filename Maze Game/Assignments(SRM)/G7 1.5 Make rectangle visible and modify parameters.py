#Task 1: Change the color of the rectangle to blue
#Task 2: Change the position of the rectangle to top left corner
#Task 3: Change the width and height of the rectangle
#Task 4: Create another rectangle at a different position
#Task 5: Try closing the pygame window by clicking on X button in window

import pygame
pygame.init()

pygame.display.set_caption("My First Game")
window = pygame.display.set_mode((600, 400))
white = (255, 255, 255)

while True:
  window.fill(white) #adding fill before draw

  pygame.draw.rect(window, (255, 255, 0), (100, 100, 30, 30))

  pygame.display.flip()
