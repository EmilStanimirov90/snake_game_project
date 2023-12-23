import pygame

pygame.init()
screen = pygame.display.set_mode((1800, 600))
pygame.display.set_caption("My Game TEST")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Fill the screen with white
    pygame.display.flip()  # Update the display

pygame.quit()