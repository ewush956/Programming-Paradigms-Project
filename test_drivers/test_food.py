# Example usage:
import math

class FoodItem:
    def __init__(self, item_id: int, x: float, y: float, z: float, energy: float):
        self.item_id = item_id   # Unique identifier for the food item
        self.x = x               # X-coordinate
        self.y = y               # Y-coordinate
        self.z = z               # Z-coordinate (elevation)
        self.energy = energy     # Energy gain when the item is reached

    @staticmethod
    def euclidean_distance(p1: tuple, p2: tuple) -> float:
        """
        Compute the Euclidean distance between two points.
        If p1 and p2 are 2-tuples, it computes 2D distance;
        If they are 3-tuples, it computes 3D distance.
        """
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

    @staticmethod
    def get_scalar1(dist_r2: float, z1: float, z2: float) -> float:
        """
        Calculate a scaling factor based on the gradient. Here, dist_r2 is the 
        2D Euclidean distance, and z1 and z2 are the elevations of the two 
        FoodItems. This function returns 1 + ((z2 - z1) / dist_r2).

        Positive Elevation Change: If the target node is at a higher elevation 
        than the current node (z2 > z1), the fraction becomes positive. Adding 
        this to 1 increases the scaling factor above 1, thereby increasing the 
        energy cost. This models the idea that moving upward is more 
        energy-intensive.

        Negative Elevation Change: Conversely, if the target node is at a lower 
        elevation (z2 < z1), the fraction becomes negative. Adding this to 1 
        decreases the scaling factor below 1, reducing the energy cost. This 
        simulates gaining an energy advantage when moving downward.
        """
        if dist_r2 == 0:
            return 1  # If we are looking at the same location.
        return 1 + ((z2 - z1) / dist_r2)

    @staticmethod
    def get_scalar2(dist_r2: float, z1: float, z2: float) -> float:
        return 1 + math.tanh(0.1 * (z2 - z1))

    @staticmethod
    def get_energy_cost(dist_r3: float, scalar: float) -> float:
        """
        Multiply the 3D distance by the scalar factor to compute the energy cost.
        """
        return dist_r3 * scalar

    def distance_to_2d(self, next_node: 'FoodItem') -> float:
        """
        Calculate the 2D Euclidean distance between this FoodItem and another using (x, y).
        """
        return FoodItem.euclidean_distance((self.x, self.y), (next_node.x, next_node.y))

    def distance_to_3d(self, next_node: 'FoodItem') -> float:
        """
        Calculate the 3D Euclidean distance between this FoodItem and another using (x, y, z).
        """
        return FoodItem.euclidean_distance((self.x, self.y, self.z), (next_node.x, next_node.y, next_node.z))

    def energy_cost_to(self, next_node: 'FoodItem') -> float:
        """
        Calculate the energy cost for the Tendril Agent to move from this FoodItem to another.
        The energy cost is based on the 3D Euclidean distance scaled by a factor that
        reflects the gradient between the two points.
        """
        # Use 2D distance for the gradient scaling factor
        dist_r2 = self.distance_to_2d(next_node)
        # Use 3D distance for the overall movement cost
        dist_r3 = self.distance_to_3d(next_node)
        # Get the scalar factor for the gradient adjustment for "uphill" vs "downhill" movement.
        scalar = FoodItem.get_scalar2(dist_r2, self.z, next_node.z)
        # Return the newly scaled 3D movement.
        return FoodItem.get_energy_cost(dist_r3, scalar)

    def __str__(self):
        return (f"FoodItem(id={self.item_id}, x={self.x}, y={self.y}, z={self.z}, energy={self.energy})")

if __name__ == "__main__":
    food_list = [
        FoodItem(0,4.0,4.0,5.0,0),
        FoodItem(1,0.0,1.0,3.0,6),
        FoodItem(2,2.0,2.0,3.0,6),
        ]

    food_start = food_list[0]
    food_next = food_list[2]

    print(f"2D Distance: {food_start.distance_to_2d(food_next):.4f}")
    print(f"3D Distance: {food_start.distance_to_3d(food_next):.4f}")
    print(f"Scaler adjustment: {food_start.get_scalar2(food_next.distance_to_2d(food_next), food_start.z, food_next.z):.4f}")
    print(f"Energy cost: {food_start.energy_cost_to(food_next):.4f}\n")