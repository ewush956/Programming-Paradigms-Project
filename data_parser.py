import csv
import matplotlib.pyplot as plt
import mpl_toolkits as mpl

filename = "random_coordinates_energy.csv"

with open(filename, mode='r', newline='') as file:
    reader = csv.DictReader(file)

    for row in reader:
        node_number = int(row['Node Number'])
        x = float(row['X'])
        y = float(row['Y'])
        z = float(row['Z'])
        energy = int(row['Energy'])

        print(f"Node Number: {node_number}, x:{x}, y: {y}, z: {z}, energy: {energy}")