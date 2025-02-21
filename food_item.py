# This is a Cartesian Plane Node.
class FoodItem():
    
    def __init__(self, food_id: int | None, x: float | None, y: float | None, z: float | None, energy: int | None) -> None:
        self._validate_inputs(food_id, x, y, z, energy)
        self.food_id = food_id
        self.x = x
        self.y = y
        self.z = z
        self.energy = energy
    
    def _validate_inputs(self, food_id, x, y, z, energy):
        """
        Validates the inputs to an instance of a FoodItem class.
        """
        if not isinstance(food_id, (int, type(None))):
            raise ValueError(f"food_id must be a positive number or None, got {type(food_id).__name__}")
        if food_id is not None and food_id < 0:
            raise ValueError(f"food_id must be a positive number, got {food_id}")
        if not isinstance(x, (int, float, type(None))):
            raise TypeError(f"x must be a numerical value, got {type(x).__name__}")
        if not isinstance(y, (int, float, type(None))):
            raise TypeError(f"y must be a numerical value, got {type(y).__name__}")
        if not isinstance(z, (int, float, type(None))):
            raise TypeError(f"z must be a numerical value, got {type(z).__name__}")
        if not isinstance(energy, (int, float, type(None))):  # Energy can be negative but must be numeric
            raise TypeError(f"energy must be a numerical value, got {type(energy).__name__}")

    def __str__(self):
        return (f"Food Id:{self.food_id}\n"
                f"X-Coord:{self.x}\n"
                f"Y-Coord:{self.y}\n"
                f"Z-Coord:{self.z}\n"
                f"Energy:{self.energy}\n")
    
    # For testing purposes
    def __eq__(self, other):
        if not isinstance(other, FoodItem):
            return False
        return (
            self.food_id == other.food_id and
            self.x == other.x and
            self.y == other.y and
            self.z == other.z and
            self.energy == other.energy
        )
