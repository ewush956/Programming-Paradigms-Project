import csv
import matplotlib.pyplot as plt
import mpl_toolkits as mpl

filename = "random_coordinates_energy.csv"

node_nums = []
x_coords = []
y_coords = []
z_coords = []
energy = []

with open(filename, mode='r', newline='') as file:
    reader = csv.DictReader(file)

    for row in reader:
        node_nums.append(int(row['Node Number']))
        x_coords.append(float(row['X']))
        y_coords.append(float(row['Y']))
        z_coords.append(float(row['Z']))
        energy.append(int(row['Energy']))


fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

marker_sizes = [10 * e for e in energy]

ax.scatter(x_coords, y_coords, z_coords, c='purple', marker='x', s=marker_sizes)

# Label each node with its energy value
for i in range(len(x_coords)):
    # Adjust fontsize and color as needed
    ax.text(x_coords[i], y_coords[i], z_coords[i], f"{node_nums[i]}", 
            fontsize=12, color='black')

ax.plot(x_coords, y_coords, z_coords, marker='o')
plt.show()