from food_item import FoodItem
from path import Path
import csv

class Graph():
    """
    The Graph class represents the problem domain for the traversal problem.
    It contains information about the available food items from the CSV dataset, the remaining 
    food that has not been "eaten", and two instances of the Path class: optimal_path (which
    represents the current best path found) and current_path (which represents the current path
    being run in the problem).
    """

    def __init__(self):
        self.optimal_path = Path()
        self.current_path = Path()
        self.remaining_food : int = []
        self.food_items = []

    def read_csv_data(self, filename : str):
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row
            for row in csv_reader:
                self.food_items.append(
                    FoodItem(int(row[0]),
                    float(row[1]), 
                    float(row[2]), 
                    float(row[3]), 
                    int(row[4])))

    def update_optimal(self):
        if(self.current_path.net_energy_gain > self.optimal_path.net_energy_gain):
            self.optimal_path = self.current_path[:]

    def update_remaining_food(self):
        pass
    