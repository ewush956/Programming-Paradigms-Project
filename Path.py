from Food_Item import FoodItem

class Path():
    """
    The Path class represents a path through the graph of food items. It contains information
    about the current food item being used, the path taken so far, and the net energy gain
    from the path.
    """
    def __init__(self):
        self.current_food_node : FoodItem = FoodItem(None, None, None, None, None) # Starts with an empty FoodItem
        ''' The current food item being used. '''
        #self.path_list : FoodItem = []
        self.path_list : int = []
        ''' A list of integers denoting the food_id of the current path '''
        self.net_energy_gain : int = 0
        ''' The total net energy gained so far in the run '''

    def __str__(self):
        #return " --> ".join(str(node) for node in self.path_list)
        return " 🍆💦  ".join(str(node) for node in self.path_list)
        #return " 👉😎👉  ".join(str(node) for node in self.path_list)
        #return " 👉 ".join(str(node) for node in self.path_list)
    
        
    