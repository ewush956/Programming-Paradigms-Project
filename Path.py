from food_item import FoodItem

class Path():
    def __init__(self):
        self.current_food_node : FoodItem = FoodItem(None, None, None, None, None) # Starts with an empty FoodItem
        ''' The current food item being used. '''
        self.path_list : FoodItem = []
        ''' A list of integers denoting the food_id of the current path '''
        self.net_energy_gain : int = 0
        ''' The total net energy gain so far in the run '''
    
    def set_starting_position(self, starting_food : FoodItem):
        self.path_list.append(starting_food)
    
    def set_current_food_item(self, current_food : FoodItem):
        self.current_food = current_food

    def add_to_path(self, node : FoodItem):
        self.path_list.append(node)
    
    def update_net(self, energy_gain : int):
        self.net_energy_gain += energy_gain

    def __str__(self):
        final_string = ""
        for node in self.path_list:
            final_string = final_string + " -> " + str(node.food_id)
        return final_string
        
    