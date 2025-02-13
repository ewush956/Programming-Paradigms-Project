import csv
import matplotlib.pyplot as plt
import mpl_toolkits as mpl
import numpy as np
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

#ax = fig.add_axes([0.0, 0.0, 1.4, 1.4], projection='3d')
ax = fig.add_axes([0.05, 0.05, 0.9, 0.9], projection='3d')
box = ax.get_position()
ax.set_position([box.x0 - 0.05, box.y0 - 0.05, box.width + 0.1, box.height + 0.1])

# max_range = np.array([max(x_coords)-min(x_coords), max(y_coords)-min(y_coords), max(z_coords)-min(z_coords)]).max() / 2.0
# mid_x = (max(x_coords) + min(x_coords)) * 0.5
# mid_y = (max(y_coords) + min(y_coords)) * 0.5
# mid_z = (max(z_coords) + min(z_coords)) * 0.5

# ax.set_xlim(mid_x - max_range, mid_x + max_range)
# ax.set_ylim(mid_y - max_range, mid_y + max_range)
# ax.set_zlim(mid_z - max_range, mid_z + max_range)
#marker_sizes = [2 * e for e in energy]


ax.scatter(x_coords, y_coords, z_coords, c='purple', marker='')

# Label each node with its energy value
for i in range(len(x_coords)):
    # Adjust fontsize and color as needed
    ax.text(x_coords[i], y_coords[i], z_coords[i], f"{node_nums[i]} ", 
    #ax.text(x_coords[i], y_coords[i], z_coords[i], f"{energy[i]}", 
            fontsize=13, color='black')

ax.plot(x_coords, y_coords, z_coords, marker='', color='grey')

# Disable built-in rotation
ax.mouse_init(rotate_btn=None)

# Variables to store starting values
start_event = None
start_azim = None
start_elev = None
ax.set_xlabel("X Axis", fontsize=14)
ax.set_ylabel("Y Axis", fontsize=14)
ax.set_zlabel("Z Axis", fontsize=14)
ax.set_title("3D Data Visualization", fontsize=16)
ax.grid(True)

sc = ax.scatter(x_coords, y_coords, z_coords, c=energy, cmap='autumn', marker='o', s=50)
plt.colorbar(sc, ax=ax, label='Energy')


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
def on_scroll(event):
    scale = 1.1 if event.button == 'down' else 1/1.1
    ax.set_xlim([x*scale for x in ax.get_xlim()])
    ax.set_ylim([y*scale for y in ax.get_ylim()])
    ax.set_zlim([z*scale for z in ax.get_zlim()])
    fig.canvas.draw_idle()

fig.canvas.mpl_connect('scroll_event', on_scroll)

def on_release(event):
    global start_event
    start_event = None

fig.canvas.mpl_connect('button_press_event', on_press)
fig.canvas.mpl_connect('motion_notify_event', on_motion)
fig.canvas.mpl_connect('button_release_event', on_release)

plt.show()