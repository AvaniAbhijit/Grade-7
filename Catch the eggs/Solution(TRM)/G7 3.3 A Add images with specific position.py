#Task 1 - Write the code for the egg postion at top of the screen.
#Task 2 - Write the code for the basket postion at the center bottom of the screen.
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Window with Images")

# Load images
background_img = pygame.image.load('bg.jpg')
background_img = pygame.transform.scale(background_img, (screen_width, screen_height))

basket_img = pygame.image.load('basket.png')
basket_width, basket_height = 100, 60
basket_img = pygame.transform.scale(basket_img, (basket_width, basket_height))

egg_img = pygame.image.load('egg.png')
egg_radius = 20
egg_img = pygame.transform.scale(egg_img, (egg_radius * 2, egg_radius * 2))

# Basket initial position
basket_x = (screen_width - basket_width) // 2
basket_y = screen_height - basket_height - 20  # Positioning the basket near the bottom of the screen

# Egg initial position
egg_x = screen_width // 2
egg_y = 50  # Positioning the egg at the top of the screen

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background image
    screen.blit(background_img, (0, 0))
    
    # Draw the basket
    screen.blit(basket_img, (basket_x, basket_y))
    
    # Draw the egg
    screen.blit(egg_img, (egg_x - egg_radius, egg_y - egg_radius))
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
