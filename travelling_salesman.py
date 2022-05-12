import pygame
# import math
# import random
from classes.salesman import Population
from classes.bruteforce import Bruteforce
from classes.csv_writing import csv_writing

pygame.init()


def update():
    pygame.display.update()


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


def draw_text(t, color, pos):
    global screen
    myFont = pygame.font.Font(None, 20)
    text = str(t)
    renderFont = myFont.render(text, 1, color)
    screen.blit(renderFont, pos)


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Window dimensions
WIDTH = 800
HEIGHT = 700

# Variables
cities = []
population_size = 100
population = None
random_tester = None

csv_writer = None

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
            # print(random_tester.best_route)
            all_cities_added = True
            population = Population(population_size, cities)
            random_tester = Bruteforce(cities)
            csv_writer = csv_writing(
                "csv_files/pop_size" + str(population_size) + ".csv", open_path=True)

    # Stuff
    if all_cities_added:
        best_salesman = population.generate_next_population(0.6)
        pop_route = best_salesman.route
        random_route = random_tester.test_random_route()

        draw_route(pop_route, cities, route_color=(255, 255, 255), thickness=3)
        draw_route(random_route, cities, route_color=(0, 0, 255), thickness=1)

        draw_text(best_salesman.dist_sq, (255, 255, 255), (10, 10))
        draw_text(random_tester.best_dist_sq, (0, 0, 255), (10, 30))
        draw_text("gen " + str(population.generation),
                  (255, 255, 255), (10, 50))

        if population.generation % 20 == 0:
            csv_writer.add_line([population.generation, best_salesman.dist_sq])

    update()


# Quit
csv_writer.close_file()
print("Quitting")
pygame.quit()
