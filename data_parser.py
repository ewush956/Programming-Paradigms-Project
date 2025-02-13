import csv
import matplotlib.pyplot as plt
import mpl_toolkits as mpl

filename = "solution.csv"

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

ax.scatter(x_coords, y_coords, z_coords, c='purple', marker='o', s=marker_sizes)

# Label each node with its energy value
for i in range(len(x_coords)):
    # Adjust fontsize and color as needed
    ax.text(x_coords[i], y_coords[i], z_coords[i], f"{node_nums[i]}", 
    #ax.text(x_coords[i], y_coords[i], z_coords[i], f"{energy[i]}", 
            fontsize=12, color='black')

ax.plot(x_coords, y_coords, z_coords, marker='o')

# Disable built-in rotation
ax.mouse_init(rotate_btn=None)

# Variables to store starting values
start_event = None
start_azim = None
start_elev = None

def on_press(event):
    global start_event, start_azim, start_elev
    if event.inaxes == ax:
        start_event = event
        start_azim = ax.azim
        start_elev = ax.elev

def on_motion(event):
    global start_event, start_azim, start_elev
    if start_event is None or event.inaxes != ax:
        return
    dx = event.x - start_event.x
    dy = event.y - start_event.y
    # Only update the dominant direction:
    if abs(dx) > abs(dy):
        new_azim = start_azim - dx * 0.5
        new_elev = start_elev
    else:
        new_elev = start_elev - dy * 0.5
        new_azim = start_azim
    ax.view_init(elev=new_elev, azim=new_azim)
    fig.canvas.draw_idle()

def on_release(event):
    global start_event
    start_event = None

fig.canvas.mpl_connect('button_press_event', on_press)
fig.canvas.mpl_connect('motion_notify_event', on_motion)
fig.canvas.mpl_connect('button_release_event', on_release)

plt.show()