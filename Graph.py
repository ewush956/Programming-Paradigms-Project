import csv
import bisect
import time

import matplotlib.pyplot as plt

from Food import FoodItem
from Data import Data
from Path import Path
from proj_math import get_total_cost

class Graph:
    def __init__(self, 
                 seed : int | None = None,
                 visual_delay : float = 0.00001,
                 starting_node_index : int = 0,
                 live_plot : bool = False,
                 path_printing : bool = False,
                 show_final_graph : bool = False,
                 optimal_update : bool = False,
                 path_update : bool = False,
                 input_file : str = "random_coordinates_energy.csv",
                 output_file : str = "solution.csv") -> None:
        """
        The Graph class represents the problem domain for the traversal problem.
        It contains information about the available food items from the CSV dataset,
        the remaining food that has not been "eaten", and two instances of the 
        Path class: optimal_path (which represents the current best path found) and 
        current_path (which represents the current path being run in the problem).

        Args:
            seed: Set random seed for reproducibility.
            visual_delay: The delay between each step in the visualization.
            starting_node_index: The starting node id from the coordinates.
            live_plot: If you would like to see live plotting of the program.
            path_printing: Prints the current path to the console.
            optimal_update: Print the current optimal path when it is updated.
            path_update: Print the current full path found.
            input_file: The CSV file containing the food item data.
            output_file: The CSV file to write the solution to.
        """
        self.valid = True
        self.solution_count = 0
        self.optimal_path = Path()
        self.current_path = Path()
        self.data = Data(seed=seed,
                         visual_delay=visual_delay,
                         starting_node=starting_node_index,
                         input_data_file=input_file,
                         output_data_file=output_file)
        self.remaining_food: list[int] = []
        self.all_food_nodes: list[FoodItem] = []
        self.min_energy_needed: int = 0
        self.solution_start_time = 0
        self.solution_end_time = 0
        self.live_plot = live_plot
        self.show_final_graph = show_final_graph
        self.path_printing = path_printing
        self.optimal_update = optimal_update
        self.path_update = path_update 
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
            self.solution_count += 1
            self.update_optimal()
            if self.path_update:
                print(
                    f"\nFound A Path: {self.current_path.path_list}\n"
                    f"Net Energy Remaining: {self.current_path.net_energy_gain:.4f}\n"
                    )
            return 
            

        for food_id in list(self.remaining_food):
            next_food_item = self.all_food_nodes[food_id]
            cost = get_total_cost(food_item, next_food_item)

            if self.current_path.net_energy_gain >= cost:
                self.move_forward(next_food_item, cost)
                time.sleep(self.data.visual_delay)
                self.pause_and_update()
                self.solve(next_food_item)
                self.backtrack(next_food_item, cost)
                time.sleep(self.data.visual_delay)
                self.pause_and_update()
                    
    def pause_and_update(self) -> None:
        """
        Pauses execution for the visual delay and updates the plot if live plotting is enabled.
        """
        time.sleep(self.data.visual_delay)
        if self.live_plot:
            self.data.update_plot(graph=self)

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

        # Prepare the starting state
        self.prepare_starting_state()
        
        # Start timer and find the minimum starting energy
        self.solution_start_time = time.time()
        
        # Get the minimum energy needed to solve the problem by 
        # finding the optimal path with the least energy needed.
        if find_min:
            self.min_energy_needed = self.solver_find_min_energy(starting_energy, 
                                                                 max_energy)
        else:
            # Alternative attempt to solve with just starting minimum energy
            self.current_path.net_energy_gain = self.all_food_nodes[0].energy
            self.min_energy_needed = starting_energy
            self.solve(self.all_food_nodes[self.starting_node_index])
        
        # Stop timer
        self.solution_end_time = time.time()

    def prepare_starting_state(self) -> None:
        # Remove the starting node from the remaining food list
        self.remaining_food.remove(self.starting_node_index)
        # Add the starting node to the path
        self.current_path.path_list.append(self.starting_node_index)

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
        try:
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
        except FileNotFoundError:
            self.valid = False
            if filename == '':
                #self.valid = False
                print("\nNo File specified, provide a file directory")
                print(r'python .\main.py --input_file ".\test_cases\file_name.csv" ')
                print("or use --create_random_data to generate random data\n")
            else:
                print(f"Error: The file '{filename}' was not found.")
        except ValueError as e:
            print(f"Error: Invalid data format in file '{filename}'. {e}")
        except Exception as e:
            print(f"An unexpected error occurred while reading the file '{filename}': {e}")
        finally:
            print(f"Finished attempting to read the file '{filename}'.")
    
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
            if self.optimal_update:
                print(
                    f"\nCurrent Optimal Path: {self.optimal_path.path_list}\n"
                    f"Net Energy Remaining: {self.optimal_path.net_energy_gain:.4f}\n"
                )
    
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
                f"✅ Found {self.solution_count} solutions\n"
                f"✅ Minimum Starting Energy Needed To Solve: {self.min_energy_needed}\n"
                f"✅ Optimal Path: {self.optimal_path}\n"
                f"✅ Net Energy Remaining: {self.optimal_path.net_energy_gain:.4f}\n"
                )
        print(results)

    def run(self, num_points=5,
        find_min=False, create_random_data=False,
        starting_energy = 1, max_energy = 30,
        x_lower_limit=0, x_upper_limit=10,
        y_lower_limit=0, y_upper_limit=10,
        z_lower_limit=0, z_upper_limit=5,
        energy_lower_limit=1, energy_upper_limit=5):

      # Wrap all the limit parameters into a dictionary
      limits = {"xll": x_lower_limit, "xul": x_upper_limit,
            "yll": y_lower_limit, "yul": y_upper_limit,
            "zll": z_lower_limit, "zul": z_upper_limit,
            "ell": energy_lower_limit, "eul": energy_upper_limit,}

      if create_random_data:
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        self.data.input_data_file = "create_random_data.csv"
        self.data.create_random_data(num_points=num_points, **limits)
      
        """ Read random data from default CSV file or user specified file """
      self.read_csv_data(filename=self.data.input_data_file)
      
      """ Initialize remaining food list from data """
      self.initialize_remaining_food()
      
      if self.is_valid_starting_node():
        self.setup_solver(starting_energy=starting_energy, 
                           max_energy=max_energy, find_min=find_min)
        
        self.write_solution_to_csv(filename=self.data.output_data_file)
        self.results_print()
        if self.show_final_graph:
            self.data.plot_solution()
            self.data.show_final_plot()
