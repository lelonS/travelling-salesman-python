# Salesman class
import random


class Salesman:
    route = []
    dist_sq = -1

    def __init__(self, amount_cities, random_path=True, route=[]):
        # Create from premade route
        if route != []:
            self.route = route
            return

        # Create route
        self.route = []
        for i in range(amount_cities):
            self.route.append(i)
        if random_path:
            random.shuffle(self.route)

    def swap(self, a, b):
        temp = self.route[a]
        self.route[a] = self.route[b]
        self.route[b] = temp

    def swap_random(self):
        if len(self.route) < 2:
            return
        i_1 = random.randint(0, len(self.route) - 1)
        i_2 = random.randint(0, len(self.route) - 1)
        while i_2 == i_1:
            i_2 = random.randint(0, len(self.route) - 1)
        self.swap(i_1, i_2)

    def calc_distance(self, city_coords, come_back=False):
        total_squared = 0

        k = 0 if come_back else 1

        for i in range(len(self.route) - k):
            city_id_1 = self.route[i]
            city_id_2 = self.route[(i + 1) % len(self.route)]

            city_coords_1 = city_coords[city_id_1]
            city_coords_2 = city_coords[city_id_2]

            x_sq = (city_coords_2[0] - city_coords_1[0]) ** 2
            y_sq = (city_coords_2[1] - city_coords_1[1]) ** 2
            total_squared += x_sq + y_sq

        self.dist_sq = total_squared

    def combine_with(self, other, mutation):
        # TODO: MAKE SURE HAS SAME AMOUNT OF CITITES
        new_route = []
        last_from_self = True
        for i in range(len(self.route)):
            if i == 0:
                new_route.append(self.route[0])
            else:
                route_check = other.route if last_from_self else self.route
                index = route_check.index(new_route[-1])
                while index < len(route_check) * 3:
                    next_city = route_check[(index + 1) % len(route_check)]
                    index += 1
                    if next_city not in new_route:
                        new_route.append(next_city)
                        last_from_self = not last_from_self
                        break
        new_salesman = Salesman(len(new_route), route=new_route)
        max_swaps = 10
        swaps = 0
        while (random.random() < mutation):
            new_salesman.swap_random()
            swaps += 1
            if (swaps > max_swaps):
                break
        return new_salesman


class Population:
    population = []
    cities = []
    generation = 0

    def __init__(self, size, cities):
        self.cities = cities
        for i in range(size):
            self.population.append(Salesman(len(cities)))

    def get_sorted_population(self):
        sorted_population = []
        for sm in self.population:
            sm.calc_distance(self.cities)
            index = 0
            for i in range(len(sorted_population)):
                # Smallest distance first
                if (sorted_population[i].dist_sq > sm.dist_sq):
                    break
                index += 1
            sorted_population.insert(index, sm)
        return sorted_population

    # Returns best route
    def generate_next_population(self, mutation):
        new_population = []
        sorted_population = self.get_sorted_population()

        new_population.append(sorted_population[0])
        new_population.append(Salesman(len(self.cities)))
        new_population.append(Salesman(len(self.cities)))
        new_population.append(Salesman(len(self.cities)))
        new_population.append(Salesman(len(self.cities)))

        # TODO: COMBINE MORE THAN BEST 2
        i = 0
        while len(new_population) < len(self.population):
            i += 1
            new_population.append(sorted_population[0].combine_with(
                sorted_population[i], mutation))
        self.population = new_population
        self.generation += 1

        return new_population[0]
