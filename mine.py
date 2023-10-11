import pygame
import random

# Initialize Pygame
pygame.init()

# Set the width and height of the screen
WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the window
pygame.display.set_caption("My Minecraft-like Game")

# Set the colors for the player and blocks
PLAYER_COLOR = (255, 255, 0)
BLOCK_COLOR = (128, 128, 128)

# Set the size of the player and blocks
BLOCK_SIZE = 16
PLAYER_SIZE = (BLOCK_SIZE, BLOCK_SIZE)

# Set the initial position of the player
player_pos = [WIDTH // 2, HEIGHT // 2]

# Create a list of blocks
blocks = [pygame.Rect(random.randint(0, WIDTH - BLOCK_SIZE), random.randint(0, HEIGHT - BLOCK_SIZE), BLOCK_SIZE, BLOCK_SIZE) for _ in range(20)]

# Set the speed of the player and score
player_speed = 5
score = 0

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Exit the game
            pygame.quit()
            exit()

    # Handle keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    # Check for collision with blocks
    for block in blocks[:]:
            pygame.draw.rect(screen, PLAYER_COLOR, pygame.Rect(tuple(player_pos) + PLAYER_SIZE))
            # Remove the block if the player collides with it
            blocks.remove(block)
            score += 1

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the blocks
    for block in blocks:
        pygame.draw.rect(screen, BLOCK_COLOR, block)

    # Draw the player
    pygame.draw.rect(screen, PLAYER_COLOR, pygame.Rect(tuple(player_pos) + tuple(PLAYER_SIZE)))


    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

    if score >= 20:
        for _ in range(20):
            x = random.randint(0, WIDTH - BLOCK_SIZE)
            y = random.randint(0, HEIGHT - BLOCK_SIZE)
            blocks.append(pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE))
