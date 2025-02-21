# This is a Cartesian Plane Node.
class FoodItem():
    
    def __init__(self, food_id: int, x: float, y: float, z: float, energy: int) -> None:
        if not isinstance(food_id, int) or food_id <= 0:
            raise ValueError(f"food_id must be a positive , got {type(food_id).__name__}")
        if not isinstance(x, (int, float)):
            raise TypeError(f"x must be a number, got {type(x).__name__}")
        if not isinstance(y, (int, float)):
            raise TypeError(f"y must be a number, got {type(y).__name__}")
        if not isinstance(z, (int, float)):
            raise TypeError(f"z must be a number, got {type(z).__name__}")
        if not isinstance(energy, (int, float)):  # Energy can be negative but must be numeric
            raise TypeError(f"energy must be a number, got {type(energy).__name__}")

        self.food_id = food_id
        self.x = x
        self.y = y
        self.z = z
        self.energy = energy
    
    def __str__(self):
        return (f"Food Id:{self.food_id}\n"
                f"X-Coord:{self.x}\n"
                f"Y-Coord:{self.y}\n"
                f"Z-Coord:{self.z}\n"
                f"Energy:{self.energy}\n")
