import csv
import random

class Data():
    def __init__(self):
        self.seed : int | None = None
        self.input_file : str = "random_coordinates_energy"
        self.solution_file : str = "solution.csv"

    def set_random_seed(self, seed : int | None = None) -> None:
        random.seed(seed)

    filename = "random_coordinates_energy"

    def __generate_random_points(self, num_points):
        points = []
        for i in range(num_points):
            x = round(random.uniform(0, 50), 0)
            y = round(random.uniform(0, 50), 0)
            z = round(random.uniform(0, 50), 0)
            energy = random.randint(1, 50)
            if i == 0:
                points.append((i, x, y, z, 0))
            else:
                points.append((i, x, y, z, energy))
        return points

    def create_random_data(self):
        points = self.__generate_random_points(5)
        with open(self.input_file + ".csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Node Number", "X", "Y", "Z", "Energy"])
            writer.writerows(points)
    