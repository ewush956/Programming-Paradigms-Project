# This is a Cartesian Plane Node.
class FoodItem():
    
    def __init__(self, food_id: int, x: float, y: float, z: float, energy: int) -> None:
        self.food_id = food_id
        self.x = x
        self.y = y
        self.z = z
        self.energy = energy
        
    def __str__(self):
        return (f"Food Id:{self.food_id}\nX-Coord:{self.x}\nY-Coord:{self.y}\nZ-Coord:{self.z}\nEnergy:{self.energy}\n")
    
    def format_csv(self) -> str:
        return (f"{self.food_id},{self.x},{self.y},{self.z},{self.energy}")
