#Task1: Create a collision detection code with the right and left wall

import pygame

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball Example")
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define ball properties
ball_x, ball_y = 100, 100  # Initial position of the ball
ball_size = 50  # Diameter of the ball
ball_speed_x, ball_speed_y = 2, 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    #Collision detection with the top and bottom side of the screen
    if ball_y <= 0 or ball_y >= HEIGHT - ball_size:
        ball_speed_y = -ball_speed_y

    window.fill(WHITE)
    pygame.draw.ellipse(window, RED, [ball_x, ball_y, ball_size, ball_size])
    pygame.display.flip()

    pygame.time.Clock().tick(60)

# Ask student to add the ball code in our main game code .
# Add the code for ball movement with collision detection across all walls

