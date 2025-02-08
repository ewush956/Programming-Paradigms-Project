from FoodItem import FoodItem
from Path import Path
import csv

class Graph():

    def initialize_availible_food(starting_node : FoodItem):
        #everything exluding starting node
        pass
    
    def __init__(self, starting_node : FoodItem):
        self.optimal_path = Path(starting_node)
        self.current_path = Path(starting_node)
        self.food_items = []
        self.availible_food = initialize_availible_food(starting_node)


    def initialize_optimal_solution(self) -> Path:
        
        
        return optimal

    def update_optimized() -> Graph:
        pass
        
    def read_csv_data(self, filename : str):
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row
            for row in csv_reader:
                node_id = int(row[0])
                x = float(row[1])
                y = float(row[2])
                z = float(row[3])
                energy = int(row[4])
                food_item = FoodItem(node_id, x, y, z, energy)
                self.food_items.append(food_item)