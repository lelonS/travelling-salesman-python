import random


class Bruteforce:
    best_route = []
    best_dist_sq = -1

    current_route = []
    city_coords = []

    def __init__(self, city_coords):
        self.city_coords = city_coords
        for i in range(len(city_coords)):
            self.current_route.append(i)

    def test_next_route():
        pass

    def test_random_route(self):
        route = self.current_route.copy()
        random.shuffle(route)
        dist_sq = self.get_dist_sq(route)

        if dist_sq > self.best_dist_sq:
            self.best_route = route
            self.best_dist_sq = dist_sq

    def get_dist_sq(self, route, come_back=False):
        total_squared = 0

        k = 0 if come_back else 1

        for i in range(len(self.route) - k):
            city_id_1 = self.route[i]
            city_id_2 = self.route[(i + 1) % len(self.route)]

            city_coords_1 = self.city_coords[city_id_1]
            city_coords_2 = self.city_coords[city_id_2]

            x_sq = (city_coords_2[0] - city_coords_1[0]) ** 2
            y_sq = (city_coords_2[1] - city_coords_1[1]) ** 2
            total_squared += x_sq + y_sq

        if total_squared > self.best_dist_sq:
            self.best_dist_sq = total_squared
            self.best_route = route
