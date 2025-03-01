import csv
import random

import matplotlib.pyplot as plt

from food_item import FoodItem

class Data:
    """
    The Data class is responsible for generating random food item data, reading solution data,
    and plotting the 3D solution using Matplotlib. It also contains interactive controls for
    rotating the 3D plot.

    NOTE: This class is primarily only a part of the imperative project solution.
    """
    def __init__(self, 
                 seed: int | None = None, 
                 starting_node: int = 0,
                 input_data_file : str = "random_coordinates_energy.csv",
                 output_data_file : str = "solution.csv") -> None:
        
        # Set random seed for reproducibility
        random.seed(seed)

        # Starting node index
        self.starting_node = starting_node

        # Input and output data file names
        self.input_data_file = input_data_file
        self.output_data_file = output_data_file
            # Data storage for solution visualization
        self.node_nums = []

        # Coordinates and energy values for each node
        self.x_coords = []
        self.y_coords = []
        self.z_coords = []
        self.energy = []

        # Matplotlib figure & interactive elements for 3D plot
        self.fig = None

        # Matplotlib axis for 3D plot
        self.ax = None

        # Event for 3D rotation (mouse press)
        self.start_event = None

        # Initial azimuth angle (rotation around z-axis)
        self.start_azim = None   

        # Initial elevation angle (rotation around x-axis)
        self.start_elev = None

        # Delay for visualizing edges in the 3D plot (in seconds)
        self.visual_delay = 0.005

    def create_random_data(self, num_points=5,                            
                        **limits) -> None:
        """
        Create and save random food item data to a CSV file.

        Parameters:
        num_points (int): The number of food items (nodes) to generate.
        
        x_lower_limit (int): Lower bound for the x-coordinate (Default: -10).
        x_upper_limit (int): Upper bound for the x-coordinate (Default: 10).
        
        y_lower_limit (int): Lower bound for the y-coordinate (Default: -10).
        y_upper_limit (int): Upper bound for the y-coordinate (Default: 10).
        
        z_lower_limit (int): Lower bound for the z-coordinate (Default: -10).
        z_upper_limit (int): Upper bound for the z-coordinate (Default: 10).
        
        energy_lower_limit (int): Lower bound for the energy value (Default: 1).
        energy_upper_limit (int): Upper bound for the energy value (Default: 10).

        Returns:
        None. The generated data is written to the configured CSV file.
        """
        
        """Create and save random food item data to a CSV file."""
        points = self.generate_random_points(num_points, **limits)
        
        with open(file=self.input_data_file, mode="w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Node Number", "X", "Y", "Z", "Energy"])
            for food in points:
                writer.writerow([food.food_id, food.x, food.y, food.z, food.energy])
    
    def generate_random_points(self, 
                               num_points: int,
                               **limits) -> list[FoodItem]:
        """ Generate random food item data points. Set energy upper and lower limits. """
        points = []
        for i in range(num_points):
            x = round(random.uniform(limits['xll'], limits['xul']))
            y = round(random.uniform(limits['yll'], limits['yul']))
            z = round(random.uniform(limits['zll'], limits['zul']))
            energy = random.randint(limits['ell'], limits['eul'])
            """Append the food item to the list of points. 
            Set energy to 0 for the starting node."""
            points.append(FoodItem(i, x, y, z, 0
                                   if i == self.starting_node else energy))
        return points
    
    def read_solution_data(self):
        """Read the solution file and store node numbers and coordinates."""
        self.node_nums.clear()
        self.x_coords.clear()
        self.y_coords.clear()
        self.z_coords.clear()
        self.energy.clear()
        
        with open(file=self.output_data_file, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.node_nums.append(int(row['Node Number']))
                self.x_coords.append(float(row['X']))
                self.y_coords.append(float(row['Y']))
                self.z_coords.append(float(row['Z']))
                self.energy.append(int(row['Energy']))

    def _plot_nodes(self, nodes, color='blue', alpha=0.5, size=75):
        """Helper method to plot nodes."""
        x_all = [node.x for node in nodes]
        y_all = [node.y for node in nodes]
        z_all = [node.z for node in nodes]
        self.ax.scatter(x_all, y_all, z_all, c=color, alpha=alpha, s=size)

    def _plot_edges(self, path_nodes, color='black'):
        """Helper method to plot edges between nodes."""
        if len(path_nodes) > 1:
            for i in range(1, len(path_nodes)):
                start_node = path_nodes[i-1] # Previous node
                end_node = path_nodes[i] # Next node
                self.ax.plot(
                    [start_node.x, end_node.x],
                    [start_node.y, end_node.y],
                    [start_node.z, end_node.z],
                    color=color,
                    marker='o'
                )
            plt.draw()
            plt.pause(self.visual_delay)

    def update_plot(self, graph):
        """Updates the 3D plot with all food nodes and progressively draws edges with a delay."""
        if self.fig is None:
            self.fig = plt.figure()
            self.ax = self.fig.add_subplot(1, 1, 1, projection='3d')

        self.ax.clear()
        
        # Set axis labels and title
        self.ax.set_xlabel("X Axis", fontsize=12)
        self.ax.set_ylabel("Y Axis", fontsize=12)
        self.ax.set_zlabel("Z Axis", fontsize=12)
        self.ax.set_title("3D Data Visualization", fontsize=14)
        self.ax.grid(True)

        # Plot all food nodes
        self._plot_nodes(list(graph.all_food_nodes), 'blue', 0.5, 50)

        # Label each node with its node number
        for node in graph.all_food_nodes:
            self.ax.text(node.x, node.y, node.z, f" {node.food_id} ", fontsize=12, color='black')

        path_nodes = (
            [graph.all_food_nodes[node] for node in graph.current_path.path_list]
        )

        # Highlight the starting node in purple
        self._plot_nodes([graph.all_food_nodes[graph.starting_node_index]], color='purple', size=100)

        # Draw edges between nodes
        self._plot_edges(path_nodes)

        plt.draw()
        plt.pause(self.visual_delay)


    def plot_solution(self, filename: str = "solution.csv"):
        """Plot the 3D solution using Matplotlib with interactive controls."""
        self.read_solution_data()
        
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1, 1, 1, projection='3d')

        # Scatter plot of food item nodes
        sc = self.ax.scatter(self.x_coords, 
                             self.y_coords, 
                             self.z_coords, 
                             c=self.energy, 
                             cmap='cool', 
                             marker='o', 
                             alpha=1, 
                             s=75)

        # Label each node with its node number
        for i in range(len(self.x_coords)):
            self.ax.text(self.x_coords[i], 
                         self.y_coords[i], 
                         self.z_coords[i], 
                         f" {self.node_nums[i]}", 
                         fontsize=12, 
                         color='black')

        # Plot connecting path (if applicable)
        self.ax.plot(self.x_coords, self.y_coords, self.z_coords, marker='', color='grey')

        # Set axis labels and title
        self.ax.set_xlabel("X Axis", fontsize=12)
        self.ax.set_ylabel("Y Axis", fontsize=12)
        self.ax.set_zlabel("Z Axis", fontsize=12)
        self.ax.set_title("3D Data Visualization", fontsize=14)
        self.ax.grid(True)

        # plt.colorbar(sc, ax=self.ax, label='Energy', shrink=0.75)
        # Define a new axis for the colorbar, shifting it further right
        cax = self.fig.add_axes([0.9, 0.2, 0.025, 0.5])  # [left, bottom, width, height]
        cbar = plt.colorbar(sc, cax=cax, label='Energy Gain At Node')
        cbar.ax.tick_params(labelsize=10)  # Reduce font size of the labels for better readability

        # Add interactive controls
        self.fig.canvas.mpl_connect('scroll_event', self.on_scroll)
        self.fig.canvas.mpl_connect('button_press_event', self.on_press)
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_motion)
        self.fig.canvas.mpl_connect('button_release_event', self.on_release)

        plt.ioff()
        plt.show()

    def show_final_plot(self):
        """Turns off interactive mode and shows the final plot."""
        plt.ioff()

        # Close any existing figures before showing the final one
        plt.close('all')

        plt.show()

    # ========== INTERACTIVITY FUNCTIONS ==========
    def on_press(self, event):
        """Handle mouse press event to enable 3D rotation."""
        if event.inaxes == self.ax:
            self.start_event = event
            self.start_azim = self.ax.azim
            self.start_elev = self.ax.elev

    def on_motion(self, event):
        """Handle mouse drag event to rotate the 3D plot."""
        if self.start_event is None or event.inaxes != self.ax:
            return
        dx = event.x - self.start_event.x
        dy = event.y - self.start_event.y

        # Adjust azimuth and elevation based on movement
        if abs(dx) > abs(dy):
            new_azim = self.start_azim - dx * 0.5
            new_elev = self.start_elev
        else:
            new_elev = self.start_elev - dy * 0.5
            new_azim = self.start_azim
        
        self.ax.view_init(elev=new_elev, azim=new_azim)
        self.fig.canvas.draw_idle()

    def on_scroll(self, event):
        """Handle scroll event to zoom in/out."""
        scale = 1.1 if event.button == 'down' else 1/1.1
        self.ax.set_xlim([x*scale for x in self.ax.get_xlim()])
        self.ax.set_ylim([y*scale for y in self.ax.get_ylim()])
        self.ax.set_zlim([z*scale for z in self.ax.get_zlim()])
        self.fig.canvas.draw_idle()

    def on_release(self, event):
        """Handle mouse release event."""
        self.start_event = None
