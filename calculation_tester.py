from Path import Path
from FoodItem import FoodItem
from math import sqrt

def euclidean_distance_r2(x1 : int, y1 : int, x2 : int, y2 : int) -> float:
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def get_scalar(dist_r2 : float, z1 : int, z2 : int) -> float:
    return (1 + ((z2 - z1) / dist_r2))

def euclidean_distance_r3(x1 : int, y1 : int, z1 : int, x2 : int, y2 : int, z2 : int) -> float:
    return sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def get_energy_cost(dist_r3 : float, scalar : float):
    return dist_r3 * scalar

def calculate_all(node1 : FoodItem, node2 : FoodItem):
    dist_r2 = euclidean_distance_r2(node1.x, node1.y, node2.x, node2.y)
    scalar = get_scalar(dist_r2, node1.z, node2.z)
    dist_r3 = euclidean_distance_r3(node1.x, node1.y, node1.z, node2.x, node2.y, node2.z)
    energy_cost = get_energy_cost(dist_r3, scalar)
    print(f"dist_r2: {dist_r2}\nscalar: {scalar}\ndist_r3: {dist_r3}\nenergy_cost: {energy_cost}\n")

def main():
    food_item_0 = FoodItem(node_id=0, x=0, y=0, z=0, energy=4)
    food_item_1 = FoodItem(node_id=1, x=1, y=2, z=-1, energy=3)
    food_item_2 = FoodItem(node_id=2, x=1, y=4, z=5, energy=5)
    food_item_3 = FoodItem(node_id=3, x=3, y=0, z=-2, energy=2)
    food_item_4 = FoodItem(node_id=4, x=-3, y=-2, z=4, energy=6)

    calculate_all(node1 = food_item_0, node2 = food_item_3)

main()
