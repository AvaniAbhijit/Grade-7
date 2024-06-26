# Task: Add only the right wall collision detection

import pygame

WIDTH, HEIGHT = 800, 600
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

paddle_width = 100
paddle_height = 20
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - paddle_height - 20
paddle_speed = 10

# Bricks
brick_rows = 5
brick_cols = 10
brick_width = 75
brick_height = 20
brick_padding = 10
bricks = []

# Ball
ball_size = 20
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 2
ball_speed_y = 2


for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = col * (brick_width + brick_padding) + brick_padding
        brick_y = row * (brick_height + brick_padding) + brick_padding
        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))


window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Brick Game')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed

    ball_x += ball_speed_x
    ball_y += ball_speed_y


  # Ball and paddle collision
    if pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height).colliderect(
      pygame.Rect(ball_x, ball_y, ball_size, ball_size)):
        ball_speed_y = -ball_speed_y


    window.fill((255,255,255))
    pygame.draw.rect(window, BLUE, [paddle_x, paddle_y,     paddle_width, paddle_height])
    pygame.draw.ellipse(window, RED, [ball_x, ball_y, ball_size, ball_size])

    for brick in bricks:
        pygame.draw.rect(window, BLACK, brick)

    pygame.display.update()
    pygame.time.Clock().tick(60)
