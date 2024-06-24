#Task 1: The ball should reverse the direction once it hits the upper rectangular block
#Task 2: The ball should not leave the top wall once all the blocks are hit

import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Paddle properties
paddle_width = 100
paddle_height = 20
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - paddle_height - 20
paddle_speed = 10

# Brick properties
brick_rows = 5
brick_cols = 10
brick_width = 75
brick_height = 20
brick_padding = 10
bricks = []

# Ball properties
ball_size = 20
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 2
ball_speed_y = 2

# Create bricks
for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = col * (brick_width + brick_padding) + brick_padding
        brick_y = row * (brick_height + brick_padding) + brick_padding
        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

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
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball and paddle collision
    if pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height).colliderect(
            pygame.Rect(ball_x, ball_y, ball_size, ball_size)):
        ball_speed_y = -ball_speed_y

    # Ball and brick collision
    for brick in bricks[:]:  # Create a copy of the bricks list to iterate over
        if pygame.Rect(ball_x, ball_y, ball_size, ball_size).colliderect(brick):
            bricks.remove(brick)
            ball_speed_y = -ball_speed_y
            break

    # Ball and wall collision
    if ball_x < 0 or ball_x > WIDTH - ball_size:
        ball_speed_x = -ball_speed_x

    # Task 1: Ball should reverse direction once it hits the upper rectangular block
    if ball_y < 0:
        ball_speed_y = -ball_speed_y

    # Task 2: Ball should not leave the top wall once all the blocks are hit
    if not bricks and ball_y < 0:
        ball_y = 0
        ball_speed_y = abs(ball_speed_y)

    # Drawing everything
    window.fill(WHITE)
    pygame.draw.rect(window, BLUE, [paddle_x, paddle_y, paddle_width, paddle_height])
    pygame.draw.ellipse(window, RED, [ball_x, ball_y, ball_size, ball_size])

    for brick in bricks:
        pygame.draw.rect(window, BLACK, brick)

    pygame.display.update()
    pygame.time.Clock().tick(60)

