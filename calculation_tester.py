from path import Path
from food_item import FoodItem
from math import sqrt

def euclidean_distance(p1 : tuple, p2 : tuple):
    return sqrt(sum((a - b)**2 for a, b in zip(p1, p2)))

def get_scalar(dist_r2 : float, z1 : int, z2 : int) -> float:
    return (1 + ((z2 - z1) / dist_r2))

def get_energy_cost(dist_r3 : float, scalar : float):
    return dist_r3 * scalar

def valid_move(net_energy : float, node1 : FoodItem, node2 : FoodItem):
    r2 = euclidean_distance((node1.x,node1.y), (node2.x, node2.y))
    r3 = euclidean_distance((node1.x, node1.y, node1.z), (node2.x, node2.y, node2.z))
    scalar = get_scalar(r2, z1=node1.z, z2=node2.z)
    print(get_energy_cost(r3, scalar))
    return (net_energy >= get_energy_cost(r3, scalar))

def calculate_all(node1 : FoodItem, node2 : FoodItem):
    dist_r2 = euclidean_distance((node1.x, node1.y), (node2.x, node2.y))
    scalar = get_scalar(dist_r2, node1.z, node2.z)
    dist_r3 = euclidean_distance((node1.x, node1.y, node1.z), (node2.x, node2.y, node2.z))
    energy_cost = get_energy_cost(dist_r3, scalar)
    print(f"dist_r2: {dist_r2}\nscalar: {scalar}\ndist_r3: {dist_r3}\nenergy_cost: {energy_cost}\n")

def main():
    food_item_0 = FoodItem(food_id=0, x=0, y=0, z=0, energy=4)
    food_item_1 = FoodItem(food_id=1, x=1, y=2, z=-1, energy=3)
    food_item_2 = FoodItem(food_id=2, x=1, y=4, z=5, energy=5)
    food_item_3 = FoodItem(food_id=3, x=3, y=0, z=-2, energy=2)
    food_item_4 = FoodItem(food_id=4, x=-3, y=-2, z=4, energy=6)

    # calculate_all(node1 = food_item_0, node2 = food_item_3)

    print(valid_move(4, food_item_0, food_item_3))

main()
