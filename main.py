from Path import Path
from FoodItem import FoodItem
import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def get_scalar(dist_r2, z1, z2):
    return (1 + ((z2 - z1) / dist_r2))

def euclidean_distance_r3(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def get_energy_cost(dist_r3, scalar):
    return dist_r3 * scalar

def solve(path: Path) -> bool:
    pass
def main():
    path = Path()

    path.read_csv_data(filename='./random_coordinates_energy.csv')

    for fooditem in path.food_items:
        print(f"\n{fooditem}\n")
    
    print("Main")


if __name__ == "__main__":
    main()