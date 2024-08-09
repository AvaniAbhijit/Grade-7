#Task - Add background image of your choice
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Window with Background Image")

# Load background image
background_img = pygame.image.load('bg.jpg')
background_img = pygame.transform.scale(background_img, (screen_width, screen_height))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw the background image
    screen.blit(background_img, (0, 0))
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
