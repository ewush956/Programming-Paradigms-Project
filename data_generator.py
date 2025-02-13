import csv
import random

random.seed()

filename = "random_coordinates_energy"

def generate_random_points(num_points):
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

points = generate_random_points(7)

with open(filename + ".csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Node Number", "X", "Y", "Z", "Energy"])
    writer.writerows(points)
