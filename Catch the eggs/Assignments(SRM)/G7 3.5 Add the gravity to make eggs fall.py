#Task - Change the egg postion and change the gracity speed as well.
import pygame
import sys

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Falling Egg")

background_img = pygame.image.load('bg.jpg')
background_img = pygame.transform.scale(background_img, (screen_width, screen_height))

basket_img = pygame.image.load('basket.png')
basket_width, basket_height = 100, 60
basket_img = pygame.transform.scale(basket_img, (basket_width, basket_height))

egg_img = pygame.image.load('egg.png')
egg_radius = 20
egg_img = pygame.transform.scale(egg_img, (egg_radius * 2, egg_radius * 2))

basket_x = (screen_width - basket_width) // 2
basket_y = screen_height - basket_height - 20
basket_speed = 10

egg_x = screen_width // 2
egg_y = 50
egg_speed = 5  # Gravity speed for the egg

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < screen_width - basket_width:
        basket_x += basket_speed

    # Apply gravity to the egg
    egg_y += egg_speed
    if egg_y > screen_height:
        egg_y = 50  # Reset the egg position when it falls out of the screen

    screen.blit(background_img, (0, 0))
    screen.blit(basket_img, (basket_x, basket_y))
    screen.blit(egg_img, (egg_x - egg_radius, egg_y - egg_radius))

    pygame.display.flip()

pygame.quit()
sys.exit()
