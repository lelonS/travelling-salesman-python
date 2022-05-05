# Salesman class
import random


class Salesman:
    route = []
    distance_squared = -1

    def __init__(self, amount_cities, random_path=True):
        self.route = []
        for i in range(amount_cities):
            self.route.append(i)
        if random_path:
            random.shuffle(self.route)

    def calc_distance(self, city_coords, come_back=False):
        total_squared = 0
        for i in range(len(self.route) - 1):
            city_id_1 = self.route[i]
            city_id_2 = self.route[i + 1]

            city_coords_1 = city_coords[city_id_1]
            city_coords_2 = city_coords[city_id_2]

            x_sq = (city_coords_2[0] - city_coords_1[0]) ** 2
            y_sq = (city_coords_2[1] - city_coords_1[1]) ** 2
            total_squared += x_sq + y_sq
        self.distance_squared = total_squared

        # Add trip back from last point to the first point
        if come_back:
            city_id_1 = self.route[0]
            city_id_2 = self.route[-1]

            city_coords_1 = city_coords[city_id_1]
            city_coords_2 = city_coords[city_id_2]

            x_sq = (city_coords_2[0] - city_coords_1[0]) ** 2
            y_sq = (city_coords_2[1] - city_coords_1[1]) ** 2
            total_squared += x_sq + y_sq
