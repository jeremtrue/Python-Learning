import pygame
import random

# init pygame
pygame.init()

#screen
WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#title
pygame.display.set_caption("Guess the Number")

#Game variables
NumberToGuess = random.randint(1, 100)

