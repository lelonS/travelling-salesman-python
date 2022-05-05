import pygame
import math
import random
from salesman import Salesman
from bruteforce import Bruteforce

pygame.init()


def update():
    pygame.display.flip()


def draw_cities(cityPos, cityNumber=True):
    myFont = pygame.font.Font(None, 20)

    for position in cityPos:
        pygame.draw.circle(screen, (255, 255, 255), position, 2)

        if cityNumber:
            text = str(cityPos.index(position))
            renderFont = myFont.render(text, 1, (255, 255, 255))
            screen.blit(renderFont, (position[0]+4, position[1]+4))
    update()


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

# Variables
cities = []

# Loop
running = True

while running:
    # Get events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            print(pos)
            cities.append(pos)
            draw_cities(cities)

# Quit
print("Quitting")
pygame.quit()
