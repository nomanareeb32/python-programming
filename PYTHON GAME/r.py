import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("My Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the game clock
clock = pygame.time.Clock()

# Set up the player sprite
player_image = pygame.Surface((50, 50))
player_image.fill(RED)
player_rect = player_image.get_rect()
player_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    elif keys[pygame.K_RIGHT]:
        player_rect.x += 5
    elif keys[pygame.K_UP]:
        player_rect.y -= 5
    elif keys[pygame.K_DOWN]:
        player_rect.y += 5

    # Draw the game world
    window.fill(WHITE)
    window.blit(player_image, player_rect)

    # Update the game display
    pygame.display.update()

    # Control the game frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
