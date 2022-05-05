import pygame
import math
import random


def update():
    pygame.display.flip()


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Window dimensions
WIDTH = 500
HEIGHT = 500

# Make screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLACK)
update()


# Loop
running = True

while running:
    # Get events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit
print("Quitting")
pygame.quit()
