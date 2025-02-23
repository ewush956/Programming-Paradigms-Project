import csv

from Food_Item import FoodItem
from Path import Path

class Graph():
    """
    The Graph class represents the problem domain for the traversal problem.
    It contains information about the available food items from the CSV dataset,
    the remaining food that has not been "eaten", and two instances of the 
    Path class: optimal_path (which represents the current best path found) and 
    current_path (which represents the current path being run in the problem).
    """

    def __init__(self):
        self.optimal_path = Path()
        self.current_path = Path()
        self.remaining_food : int = []
        self.all_food_nodes : FoodItem = []
        self.min_energy_needed : int = 0
        self.solution_start_time = 0
        self.solution_end_time = 0

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
            print(f"Current Optimal: {self.optimal_path} \nInterim Net Gogurt Bars Retained: {self.optimal_path.net_energy_gain:.6f}\n")
            
    def initialize_remaining_food(self):
        for food in self.all_food_nodes:
            self.remaining_food.append(food.food_id)

    def print_current_path_info(self) -> None:
        """Prints the current path and net energy gain."""
        print(f"Current Path: {self.current_path}")
        print(f"Net Gogurt Bars Retained: {self.current_path.net_energy_gain}\n")
        
    def results_print(self) -> None:    
        print(f"Done! Finished in {self.solution_end_time - self.solution_start_time:.6f} seconds\n")
        if(not self.optimal_path.path_list):
            print("❌ No Optimal Path Found...\n")
        else:
            print(f"✅ Minimum Starting Gogurt Bars Needed To Finish: {self.min_energy_needed}\n") # Plus one since the min energy starts at 0.
            print(f"✅ Optimal Path: {self.optimal_path}\n --- Finished Optimal Net Gogurt Bars: {self.optimal_path.net_energy_gain:.6f}\n")
