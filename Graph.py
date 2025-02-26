import csv
import bisect
import time

import matplotlib.pyplot as plt

from Food_Item import FoodItem
from Data import Data
from Path import Path
from proj_math import get_total_cost

class Graph:
    """
    The Graph class represents the problem domain for the traversal problem.
    It contains information about the available food items from the CSV dataset,
    the remaining food that has not been "eaten", and two instances of the 
    Path class: optimal_path (which represents the current best path found) and 
    current_path (which represents the current path being run in the problem).
    """
    def __init__(self, 
                 seed : int | None = None,
                 starting_node_index : int = 0,
                 live_plot : bool = False) -> None:
        self.optimal_path = Path()
        self.current_path = Path()
        self.data = Data(seed)
        self.remaining_food: list[int] = []
        self.all_food_nodes: list[FoodItem] = []
        self.min_energy_needed: int = 0
        self.solution_start_time = 0
        self.solution_end_time = 0
        self.live_plot = live_plot
        self.starting_node_index = starting_node_index

    def solve(self, node: FoodItem) -> None:
        """
        Recursively explores paths and finds the optimal solution.

        Args:
            node (FoodItem): The current node being explored.
            data (Data): Data object for visualization.
            live_plot (bool, optional): If True, updates the plot periodically. Defaults to False.
            plot_frequency (int, optional): Number of steps between plot updates. Defaults to 10.
        """
        if not self.remaining_food:
            self.update_optimal()
            return

        for food_id in list(self.remaining_food):
            next_node = self.all_food_nodes[food_id]
            cost = get_total_cost(node, next_node)

            if self.current_path.net_energy_gain >= cost:
                # Move forward
                self.move_forward(next_node, cost)

                #print(f"Moving Forward --> :\t{self.current_path.path_list}")

                time.sleep(self.data.visual_delay)

                # Update plot visually
                if self.live_plot:
                    self.data.update_plot(graph=self)

                self.solve(next_node)

                # Backtrack
                self.backtrack(next_node, cost)

                #print(f"Backtracking <-- :\t{self.current_path.path_list}")

                time.sleep(self.data.visual_delay)

                # Update plot visually
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
        

    def backtrack(self, food_item: FoodItem, cost: float) -> None:
        """
        Backtracks the graph to explore different paths.
        """
        if food_item.food_id in self.current_path.path_list:
            self.current_path.net_energy_gain -= food_item.energy
            self.current_path.net_energy_gain += cost
            self.current_path.path_list.remove(food_item.food_id)
            bisect.insort(self.remaining_food, food_item.food_id)

    def solver_find_min_energy(self, 
                               starting_energy: int = 1, 
                               max_energy: int = 1000) -> int:
        """
        Finds the minimum starting energy needed to complete a valid path.
        """
        for energy in range(starting_energy, max_energy + 1):
            print(f"Trying energy: {energy} to start...")
            self.current_path.net_energy_gain = energy
            self.solve(self.all_food_nodes[0])
            if self.optimal_path.path_list:
                print(f"✅ Found optimal path with {energy} energy: {self.optimal_path.path_list}")
                return energy
        return max_energy  # If no valid path is found, return max_energy set.

    def setup(self,
              starting_energy: int = 1, 
              max_energy: int = 1000) -> None:
        """
        Initializes the graph, computes the optimal path, and writes the solution to a CSV file.
        """
        print("Searching for optimal path 🔎 ...\n")

        # Enable interactive mode for live updates (Optional)
        plt.ion()

        # Start timer and find the minimum starting energy
        self.solution_start_time = time.time()
        
        # Get the minimum energy needed to solve the problem by 
        # finding the optimal path with the least energy needed.
        self.min_energy_needed = self.solver_find_min_energy(starting_energy,
                                                             max_energy)
        # Stop timer
        self.solution_end_time = time.time()

        # Set minimum energy to the current path before solving
        self.current_path.net_energy_gain = self.min_energy_needed

        # # Solve again with the computed minimum energy (Optional)
        # self.solve(self.all_food_nodes[0], data, live_plot)

        # Write the solution to a CSV file
        self.write_solution_to_csv("solution.csv")

    def read_csv_data(self, filename : str):
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
    
    def write_solution_to_csv(self, filename : str):
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
        print(f"Done! Finished in {self.solution_end_time - self.solution_start_time:.6f} seconds\n")
        if(not self.optimal_path.path_list):
            print("❌ No Optimal Path Found...\n")
        else:
            print(f"✅ Minimum Starting Gogurt Bars Needed To Finish: {self.min_energy_needed}\n") # Plus one since the min energy starts at 0.
            print(f"✅ Optimal Path: {self.optimal_path}\n --- Finished Optimal Net Gogurt Bars: {self.optimal_path.net_energy_gain:.6f}\n")
