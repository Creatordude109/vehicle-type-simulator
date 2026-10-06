import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Car Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 32)

car_x = 280
car_y = 330
block_x = random.randint(0, 560)
block_y = 0
score = 0
playing = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                playing = True
            if event.key == pygame.K_ESCAPE:
                playing = False

    keys = pygame.key.get_pressed()

    if playing:
        if keys[pygame.K_LEFT] and car_x > 0:
            car_x = car_x - 5
        if keys[pygame.K_RIGHT] and car_x < 550:
            car_x = car_x + 5

        block_y = block_y + 4

        if block_y > 400:
            block_x = random.randint(0, 560)
            block_y = 0
            score = score + 1

        car = pygame.Rect(car_x, car_y, 50, 40)
        block = pygame.Rect(block_x, block_y, 40, 40)

        if car.colliderect(block):
            block_y = 0
            block_x = random.randint(0, 560)
            score = 0

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, "blue", (car_x, car_y, 50, 40))
    pygame.draw.rect(screen, "red", (block_x, block_y, 40, 40))
    screen.blit(font.render("Score: " + str(score), True, "white"), (10, 10))

    if not playing:
        screen.blit(font.render("Press SPACE to play", True, "white"), (180, 180))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
