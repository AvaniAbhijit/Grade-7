#Task: To set the ball at the centre

import pygame

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball at Centre")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_size = 50
ball_x, ball_y = WIDTH//2, HEIGHT//2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    window.fill(WHITE)
    # Draw the ball
    pygame.draw.ellipse(window, RED, [ball_x, ball_y, ball_size, ball_size])

    pygame.display.flip()
    pygame.time.Clock().tick(60)
