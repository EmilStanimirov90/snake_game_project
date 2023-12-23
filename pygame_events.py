import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space key pressed")

    screen.fill((255, 255, 255))  # Fill the screen with white
    pygame.display.flip()

pygame.quit()