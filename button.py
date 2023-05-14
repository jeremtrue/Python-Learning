import pygame

pygame.init()

# Set up the display window
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Pygame UI Example")

# Create a button rect and text
button_rect = pygame.Rect(150, 100, 100, 50)
button_text = pygame.font.Font(None, 30).render("Click Me", True, (255, 255, 255))

# Draw the button on the screen
pygame.draw.rect(screen, (0, 0, 255), button_rect)
screen.blit(button_text, button_rect.center)

# Start the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Check if the button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                print("Button Clicked!")

    pygame.display.update()
