# Salesman class
import random


class Salesman:
    route = []
    distance_squared = -1

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

        self.distance_squared = total_squared

    def combine_with(self, other):
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
        return new_route
