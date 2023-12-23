import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))

green = (91,149,88)
screen.fill((43,43,43))  # Fill the screen with white
pygame.draw.circle(screen, green, (400, 400), 30)  # Draw a red circle
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()