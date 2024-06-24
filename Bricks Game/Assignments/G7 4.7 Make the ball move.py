#Task1: Make the speed slower

import pygame

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball Example")
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define ball properties
ball_x, ball_y = 100, 100  # Initial position of the ball
ball_size = 50  # Diameter of the ball
ball_speed_x, ball_speed_y = 5, 5  # Speed of the ball in x and y directions

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    window.fill(WHITE)
    pygame.draw.ellipse(window, RED, [ball_x, ball_y, ball_size, ball_size])
    pygame.display.flip()


    pygame.time.Clock().tick(60)

#Copy the below link and teach below variation after this variation.Below variation is not available in the srm.
# Make the ball rebound after collision - Link:https://replit.com/@shushankita1/16-Make-the-ball-rebound-after-collision#main.py
