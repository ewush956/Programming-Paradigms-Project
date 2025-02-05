import csv

# This is a Cartesian Plane Node.
class FoodItem():
    
    def __init__(self, node_id: int, x: float, y: float, z: float, energy: int) -> None:
        self.node_id = node_id
        self.x = x
        self.y = y
        self.z = z
        self.energy = energy
        self.neighbours = [] # Neighbouring remaining nodes not inclusive of itself in the data.
        
    def __str__(self):
        return (f"Node Id:{self.node_id}\nX-Coord:{self.x}\nY-Coord:{self.y}\nZ-Coord:{self.z}\nEnergy:{self.energy}\nNeighbours:{self.neighbours}")
    
    def format_CSV(self) -> str:
        return (f"{self.node_id},{self.x},{self.y},{self.z},{self.energy}")
