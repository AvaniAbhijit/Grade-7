#Task 1 :  Create a collision detection code with right and left.


import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Paddle properties
paddle_width = 100
paddle_height = 20
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - paddle_height - 20
paddle_speed = 10

# Ball properties
ball_x, ball_y = 100, 100  # Initial position of the ball
ball_size = 50  # Diameter of the ball
ball_speed_x, ball_speed_y = 5, 5

# Set up display
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Brick Game')

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        paddle_x += paddle_speed
        if paddle_x + paddle_width > WIDTH:
            paddle_x = WIDTH - paddle_width
    if keys[pygame.K_LEFT]:
        paddle_x -= paddle_speed
        if paddle_x < 0:
            paddle_x = 0

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Collision detection with top and bottom walls
    if ball_y <= 0 or ball_y >= HEIGHT - ball_size:
        ball_speed_y = -ball_speed_y

    # Collision detection with left and right walls
    if ball_x <= 0 or ball_x >= WIDTH - ball_size:
        ball_speed_x = -ball_speed_x

    # Update display
    window.fill(WHITE)
    pygame.draw.rect(window, BLUE, [paddle_x, paddle_y, paddle_width, paddle_height])
    pygame.draw.ellipse(window, RED, [ball_x, ball_y, ball_size, ball_size])
    pygame.display.flip()

    pygame.time.Clock().tick(60)


# Ask student to add the ball code in our main game code .
# Add the code for ball movement with collision detection across all walls

