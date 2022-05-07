import pygame
# import math
# import random
from salesman import Population
from bruteforce import Bruteforce

pygame.init()


def update():
    pygame.display.flip()


def draw_cities(city_pos, city_number=True):
    global screen
    myFont = pygame.font.Font(None, 20)

    for position in city_pos:
        # Draw point
        pygame.draw.circle(screen, (255, 0, 0), position, 2)

        # Draw index
        if city_number:
            text = str(city_pos.index(position))
            renderFont = myFont.render(text, 1, (255, 255, 255))
            screen.blit(renderFont, (position[0]+4, position[1]+4))


def draw_route(route, city_pos, route_color=(255, 255, 255), thickness=1):
    global screen
    # print(route)
    for i in range(len(route)-1):
        c_id_1 = route[i]
        c_id_2 = route[i + 1]
        pygame.draw.line(screen, route_color,
                         city_pos[c_id_1], city_pos[c_id_2], width=thickness)


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Window dimensions
WIDTH = 500
HEIGHT = 500

# Variables
cities = []
population_size = 100
population = None
random_tester = None

# Loop
running = True
all_cities_added = False


# Make screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLACK)
update()


while running:
    # Clear screen
    screen.fill(BLACK)
    draw_cities(cities)

    # Get events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif pygame.mouse.get_pressed()[0] and not all_cities_added:
            pos = pygame.mouse.get_pos()
            cities.append(pos)
            draw_cities(cities)
        elif pygame.mouse.get_pressed()[2]:
            all_cities_added = True
            population = Population(population_size, cities)
            random_tester = Bruteforce(cities)

    # Stuff
    if all_cities_added:
        draw_route(population.generate_next_population(
            0.6).route, cities, thickness=3)
        draw_route(random_tester.test_random_route(),
                   cities, route_color=(0, 0, 255), thickness=1)

    update()


# Quit
print("Quitting")
pygame.quit()
