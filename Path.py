from FoodItem import FoodItem
import csv

class Path():
    def __init__(self, starting_food : FoodItem):
        self.path_list = [starting_food.node_id]
        self.net_energy_gain = [starting_food.energy]
    
        