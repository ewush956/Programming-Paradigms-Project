# This is a Cartesian Plane Node.
class FoodItem():
    """
    Represents a food item on a 3D Cartesian plane with an energy attribute.
    """
    def __init__(self, 
                 food_id: int | None, 
                 x: float | None, 
                 y: float | None, 
                 z: float | None, 
                 energy: int | None) -> None:
        """
        Initializes a FoodItem object with the given food_id, x, y, z, and energy.

        Args:
            food_id: A positive integer (Any value >= 0) representing the food item's ID.
            x: A numerical value representing the food item's x-coordinate.
            y: A numerical value representing the food item's y-coordinate.
            z: A numerical value representing the food item's z-coordinate.
            energy: A numerical value representing the food item's energy.
        """
        self._validate_inputs(food_id, x, y, z, energy)
        self.food_id = food_id
        self.x = x
        self.y = y
        self.z = z
        self.energy = energy
    
    @staticmethod
    def _validate_inputs(food_id, x, y, z, energy) -> None:
        """
        Validates the inputs to an instance of a FoodItem class.

        Ensures that:
        - food_id is either a positive integer or None.
        - x, y, and z are numerical values (int/float) or None.
        - energy is a numerical value (int/float) or None.

        Raises:
            ValueError: If food_id is negative.
            TypeError: If any input is of an incorrect type.
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

    def __str__(self) -> str:
        """
        Returns a string representation of the FoodItem object.
        """
        return (f"Food Item {self.food_id if self.food_id is not None else 'N/A'}\n"
                f"------------\n"
                f"X-Coord:{self.x if self.x is not None else 'N/A'}\n"
                f"Y-Coord:{self.y if self.y is not None else 'N/A'}\n"
                f"Z-Coord:{self.z if self.z is not None else 'N/A'}\n"
                f"Energy:{self.energy if self.energy is not None else 'N/A'}\n")
    
    def __eq__(self, other) -> bool:
        """
        Compares if two FoodItem objects are equal.

        Two FoodItem objects are considered equal if:
        - They have the same food_id, coordinates (x, y, z), and energy values.

        Args:
            other: Another object to compare against.

        Returns:
            True if both objects have identical attributes, otherwise
            False if either they are not equal or the other object is not of a
            FoodItem class type.
        """
        if not isinstance(other, FoodItem):
            return False
        return (
            self.food_id == other.food_id and
            self.x == other.x and
            self.y == other.y and
            self.z == other.z and
            self.energy == other.energy
        )
