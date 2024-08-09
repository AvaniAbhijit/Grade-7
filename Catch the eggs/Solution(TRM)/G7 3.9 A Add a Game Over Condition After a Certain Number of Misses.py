import pygame
import sys
import random

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Collect Eggs Game")

background_img = pygame.image.load('bg.jpg')
background_img = pygame.transform.scale(background_img, (screen_width, screen_height))

basket_img = pygame.image.load('basket.png')
basket_width, basket_height = 100, 60
basket_img = pygame.transform.scale(basket_img, (basket_width, basket_height))

basket_x = (screen_width - basket_width) // 2
basket_y = screen_height - 2 * basket_height
basket_speed = 5

egg_img = pygame.image.load('egg.png')
egg_radius = 20
egg_img = pygame.transform.scale(egg_img, (egg_radius * 2, egg_radius * 2))

# Slower fall speed for eggs
egg_speed = 5
eggs = []

# Score initialization
score = 0
font = pygame.font.Font(None, 36)

# Missed eggs initialization
missed_eggs = 0
missed_limit = 5  # Game over if the player misses 5 eggs

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < screen_width - basket_width:
        basket_x += basket_speed

    # Increase the range to reduce the number of eggs falling
    if random.randint(1, 100) == 1:
        egg_x = random.randint(egg_radius, screen_width - egg_radius)
        egg_y = 0
        eggs.append((egg_x, egg_y))

    updated_eggs = []
    for egg_x, egg_y in eggs:
        updated_y = egg_y + egg_speed
        
        # Collision detection: check if the egg is within the basket
        if basket_x < egg_x < basket_x + basket_width and basket_y < updated_y < basket_y + basket_height:
            score += 1  # Increase score when egg is caught
        elif updated_y > screen_height:  # Check if the egg falls past the basket (missed)
            missed_eggs += 1
            if missed_eggs >= missed_limit:
                game_over = True
        else:
            updated_eggs.append((egg_x, updated_y))

    eggs = updated_eggs

    screen.blit(background_img, (0, 0))
    screen.blit(basket_img, (basket_x, basket_y))
    for egg_x, egg_y in eggs:
        screen.blit(egg_img, (egg_x - egg_radius, egg_y - egg_radius))
    
    # Display score and missed eggs count
    score_surface = font.render(f"Score: {score}", True, (0, 0, 0))
    missed_surface = font.render(f"Missed: {missed_eggs}", True, (255, 0, 0))
    screen.blit(score_surface, (10, 10))
    screen.blit(missed_surface, (10, 50))

    pygame.display.flip()

    # Check if game over condition is met
    if missed_eggs >= missed_limit:
        break  # Exit the game loop if too many eggs are missed

    # Control frame rate
    clock.tick(30)

# Display "Game Over" message
screen.fill((255, 255, 255))
game_over_surface = font.render("Game Over", True, (255, 0, 0))
game_over_rect = game_over_surface.get_rect(center=(screen_width // 2, screen_height // 2))
screen.blit(game_over_surface, game_over_rect)
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
