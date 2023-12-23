import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

player_image = pygame.image.load('player.png')
player_rect = player_image.get_rect()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Fill the screen with white
    screen.blit(player_image, player_rect)  # Draw player image
    pygame.display.flip()

pygame.quit()