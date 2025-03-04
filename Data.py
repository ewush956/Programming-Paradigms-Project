import csv
import random

from Food import FoodItem

class Data:
    """
    The Data class is responsible for generating random food item data, reading solution data,
    and plotting the 3D solution using Matplotlib. It also contains interactive controls for
    rotating the 3D plot.

    NOTE: This class is primarily only a part of the imperative project solution.
    """
    def __init__(self, 
                 seed: int | None = None,
                 visual_delay: float = 0.005, 
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
        
        # Delay for visualizing edges in the 3D plot (in seconds)
        self.visual_delay = visual_delay

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
