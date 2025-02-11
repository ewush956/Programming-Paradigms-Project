import csv
import random

random.seed(42069)

filename = "random_coordinates_energy_modded"

def generate_random_points(num_points):
    points = []
    for i in range(num_points):
        x = round(random.uniform(0, 20), 2)
        y = round(random.uniform(0, 20), 2)
        z = round(random.uniform(0, 20), 2)
        energy = random.randint(1, 10)
        points.append((i, x, y, z, energy))
    return points

points = generate_random_points(10)

with open(filename + ".csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Node Number", "X", "Y", "Z", "Energy"])
    writer.writerows(points)
