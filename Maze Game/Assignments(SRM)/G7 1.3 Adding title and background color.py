#Task 1: Change the title of the game to "Maze Game"
#Task 2: Change the color of the background to red
#Task 3: Change the variable white to black in line 10 and make changes in line 13 to remvoe the error

import pygame
pygame.init()

window = pygame.display.set_mode([500, 500])
pygame.display.set_caption("My First Game") #setting the name of the window
white=(255,255,255) #giving rgb values for the color

while True:
  window.fill(white) #adding background color as white to the window
  pygame.display.flip()
