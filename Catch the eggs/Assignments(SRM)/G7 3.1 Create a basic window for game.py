import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Basic Pygame Window")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with a color (RGB format)
    screen.fill((173, 216, 230))  # Light blue background
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
