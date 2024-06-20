#Task 1: Run the program and click on X button of window to close
#Task 2: Read the condition in lines 14 to 16 to understand the logic.


import pygame

pygame.init()

pygame.display.set_caption("My First Game")
window = pygame.display.set_mode((600, 400))
white = (255, 255, 255)

while True:
  for event in pygame.event.get(): #checks for event in each iteration
   if event.type == pygame.QUIT:  #if user clicks on the close button (X)
     pygame.quit()  #Close the pygame window

  window.fill(white)
  pygame.draw.rect(window, (255, 255, 0), (100, 100, 50, 50))

  pygame.display.flip()
