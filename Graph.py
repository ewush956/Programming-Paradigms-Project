import csv
import bisect
import time

import matplotlib.pyplot as plt

from food_item import FoodItem
from data import Data
from path import Path
from proj_math import get_total_cost

class Graph:
    def __init__(self, 
                 seed : int | None = None,
                 starting_node_index : int = 0,
                 live_plot : bool = False,
                 path_printing : bool = False,
                 optimal_update : bool = False,
                 input_file : str = "random_coordinates_energy.csv",
                 output_file : str = "solution.csv") -> None:
        """
        The Graph class represents the problem domain for the traversal problem.
        It contains information about the available food items from the CSV dataset,
        the remaining food that has not been "eaten", and two instances of the 
        Path class: optimal_path (which represents the current best path found) and 
        current_path (which represents the current path being run in the problem).

        Args:
            seed: Set random seed for reproducibility (default = None).
            starting_node_index: The starting node id from the coordinates.
            live_plot: If you would like to see live plotting of the program.
            optimal_update: Print the current optimal path when it is updated.
            input_file: The CSV file containing the food item data.
            output_file: The CSV file to write the solution to.
        """
        self.optimal_path = Path()
        self.current_path = Path()
        self.data = Data(seed=seed,
                         starting_node=starting_node_index,
                         input_data_file=input_file,
                         output_data_file=output_file)
        self.remaining_food: list[int] = []
        self.all_food_nodes: list[FoodItem] = []
        self.min_energy_needed: int = 0
        self.solution_start_time = 0
        self.solution_end_time = 0
        self.live_plot = live_plot
        self.path_printing = path_printing
        self.optimal_update = optimal_update
        self.starting_node_index = starting_node_index

    def is_valid_starting_node(self) -> bool:
        return (self.starting_node_index in self.remaining_food)

    def solve(self, food_item: FoodItem) -> None:
        """
        Recursively explores paths and finds the optimal solution.

        Args:
            node (FoodItem): The current node being explored. 
            Such as the starting food_item or the next food_item.
        """
        if not self.remaining_food:
            self.update_optimal()
            if self.optimal_update:
                print(
                    f"\nFound A Path: {self.current_path.path_list}\n"
                    f"Net Energy Remaining: {self.current_path.net_energy_gain:.6f}\n"
                    )
            return

        for food_id in list(self.remaining_food):
            next_food_item = self.all_food_nodes[food_id]
            cost = get_total_cost(food_item, next_food_item)

            if self.current_path.net_energy_gain >= cost:

                self.move_forward(next_food_item, cost)

                time.sleep(self.data.visual_delay)

                if self.live_plot:
                    self.data.update_plot(graph=self)

                self.solve(next_food_item)

                self.backtrack(next_food_item, cost)

                time.sleep(self.data.visual_delay)

                if self.live_plot:
                    self.data.update_plot(graph=self)

    """ Solve method without live plotting or printing """
    # def solve(self, food_item: FoodItem) -> None:
    #     """
    #     Recursively explores paths and finds the optimal solution.

    #     Args:
    #         node (FoodItem): The current node being explored. 
    #         Such as the starting food_item or the next food_item.
    #     """
    #     if not self.remaining_food:
    #         self.update_optimal()
    #         if self.optimal_update:
    #             return

    #     for food_id in list(self.remaining_food):
    #         next_food_item = self.all_food_nodes[food_id]
    #         cost = get_total_cost(food_item, next_food_item)

    #         if self.current_path.net_energy_gain >= cost:
    #             self.move_forward(next_food_item, cost)
    #             self.solve(next_food_item)
    #             self.backtrack(next_food_item, cost)

    def move_forward(self, food_item: FoodItem, cost: float) -> None:
        """
        Moves the graph forward by updating the current path, net energy gain, 
        and remaining food list.
        """
        if food_item.food_id in self.remaining_food:
            self.remaining_food.remove(food_item.food_id)
            self.current_path.path_list.append(food_item.food_id)
            self.current_path.net_energy_gain -= cost
            self.current_path.net_energy_gain += food_item.energy

        if self.path_printing:
            print(f"Moving Forward --> :\t{self.current_path.path_list}\n")
        
    def backtrack(self, food_item: FoodItem, cost: float) -> None:
        """
        Backtracks the graph to explore different paths.
        """
        if food_item.food_id in self.current_path.path_list:
            self.current_path.net_energy_gain -= food_item.energy
            self.current_path.net_energy_gain += cost
            self.current_path.path_list.remove(food_item.food_id)
            bisect.insort(self.remaining_food, food_item.food_id)
        
        if self.path_printing:
            print(f"Backtracking <-- :\t{self.current_path.path_list}\n")

    def solver_find_min_energy(self, 
                               starting_energy: int = 1, 
                               max_energy: int = 100) -> int:
        """
        Iteratively finds the minimum starting energy needed to complete a valid path
        using the given bounds.
        """
        for energy in range(starting_energy, max_energy + 1):
            print(f"Trying energy: {energy} to start...")
            self.current_path.net_energy_gain = energy
            self.solve(self.all_food_nodes[self.starting_node_index])
            if self.optimal_path.path_list:
                print(f"\n✅ Found an optimal path with {energy} energy\n")
                return energy
        return max_energy  # If no valid path is found, return max_energy set.

    def setup_solver(self,
              starting_energy: int = 1, 
              max_energy: int = 100,
              find_min : bool = True) -> None:
        """
        Initializes the graph, computes the optimal path, 
        and writes the solution to a CSV file.
        """
        print("Searching for optimal path 🔎 ...\n")

        # Enable interactive mode for live updates (Optional)
        plt.ion()
        
        # Remove the starting node from the remaining food list
        self.remaining_food.remove(self.starting_node_index)
        
        # Add the starting node to the path
        self.current_path.path_list.append(self.starting_node_index)

        # Start timer and find the minimum starting energy
        self.solution_start_time = time.time()
        
        # Get the minimum energy needed to solve the problem by 
        # finding the optimal path with the least energy needed.
        if find_min:
            self.min_energy_needed = self.solver_find_min_energy(starting_energy, 
                                                                 max_energy)
        else:
            # Alternative attempt to solve with just starting minimum energy
            self.current_path.net_energy_gain = starting_energy
            self.min_energy_needed = starting_energy
            self.solve(self.all_food_nodes[self.starting_node_index])
        
        # Stop timer
        self.solution_end_time = time.time()

    def read_csv_data(self, filename: str = None) -> None:
        """
        Reads a CSV file containing food item data and populates 
        the 'all_food_nodes' list with FoodItem objects.

        The CSV file MUST include a header row followed by one row 
        per food item. The expected header and corresponding data 
        columns are as follows:

            Node Number, X, Y, Z, Energy

            <followed by your row-by-row, comma separated data>

        where:
            - Node Number: An integer that uniquely identifies the food item.
            Node numbers start from 0 and increment by 1.
            - X: A floating-point number representing the x-coordinate in the 3D space.
            - Y: A floating-point number representing the y-coordinate in the 3D space.
            - Z: A floating-point number representing the z-coordinate in the 3D space.
            - Energy: An integer representing the energy value for the food item.

        The function skips the header row and then reads each subsequent row, converting the string
        values into the appropriate types before instantiating a FoodItem object.

        Args:
            filename (str): The path to the CSV file containing the food item data.
        """
        if filename is None:
            filename = self.data.input_data_file
        
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row
            for row in csv_reader:
                self.all_food_nodes.append(
                    FoodItem(int(row[0]),
                    float(row[1]),
                    float(row[2]),
                    float(row[3]),
                    int(row[4])))
    
    def write_solution_to_csv(self, filename: str = None):
        if filename is None:
            filename = self.data.output_data_file
        
        with open(filename, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Node Number', 'X', 'Y', 'Z','Energy',])
            for food_item in self.optimal_path.path_list:
                csv_writer.writerow([
                    self.all_food_nodes[food_item].food_id,
                    self.all_food_nodes[food_item].x,
                    self.all_food_nodes[food_item].y,
                    self.all_food_nodes[food_item].z,
                    self.all_food_nodes[food_item].energy
                ])
    
    def update_optimal(self):
        if(self.current_path.net_energy_gain >= self.optimal_path.net_energy_gain):
            self.optimal_path.path_list = self.current_path.path_list[:]
            self.optimal_path.net_energy_gain = self.current_path.net_energy_gain 
    
    def initialize_remaining_food(self):
        """Ensure the first food item is set as the starting node."""
        self.remaining_food = [food.food_id for food in self.all_food_nodes]

    def results_print(self) -> None:
        elapsed_time = self.solution_end_time - self.solution_start_time
        if not self.optimal_path.path_list:
            results = (
                f"Done! Finished in {elapsed_time:.6f} seconds\n\n"
                f"❌ No Optimal Path Found...\n"
                )
        else:
            results = (
                f"Done! Finished in {elapsed_time:.6f} seconds\n\n"
                f"✅ Minimum Starting Energy Needed To Solve: {self.min_energy_needed}\n"
                f"✅ Optimal Path: {self.optimal_path}\n"
                f"✅ Net Energy Remaining: {self.optimal_path.net_energy_gain:.6f}\n"
                )
        print(results)
