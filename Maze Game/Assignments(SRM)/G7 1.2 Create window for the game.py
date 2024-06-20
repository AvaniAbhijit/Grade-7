#Task: Modify the size of the window - Change width and then height

import pygame
pygame.init()

window = pygame.display.set_mode([500, 500])

while True: #adding a loop to make sure window keeps updating screen forever
  pygame.display.flip() #function to update content of the entire screen
