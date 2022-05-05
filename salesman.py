# Salesman class
import random


class Salesman:
    route = []

    def __init__(self, amount_cities, random_path=True):
        self.route = []
        for i in range(amount_cities):
            self.route.append(i)
        if random_path:
            random.shuffle(self.route)
        print(self.route)
