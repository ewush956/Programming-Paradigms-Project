from FoodItem import FoodItem
import csv

class Path():
    def __init__(self):
        self.food_items = []
        
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