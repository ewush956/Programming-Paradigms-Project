from Food_Item import FoodItem
from math import sqrt
from math import tanh

def euclidean_distance(p1 : tuple, p2 : tuple):
    return sqrt(sum((a - b)**2 for a, b in zip(p1, p2)))

def get_scalar(dist_r2 : float, start : int, final : int) -> float:
    #if dist_r2 == 0:
    #    return 1
    #return (1 + ((z2 - z1) / dist_r2))
    return (1 + (tanh(0.1*(final - start))))

def get_energy_cost(dist_r3 : float, scalar : float):
    return dist_r3 * scalar

def valid_move(net_energy : float, starting_node : FoodItem, target_node : FoodItem):
    return (net_energy >= get_total_cost(starting_node, target_node))

def get_total_cost(starting_node : FoodItem, target_node : FoodItem) -> int:
    r2 = euclidean_distance((starting_node.x,starting_node.y), (target_node.x, target_node.y))
    r3 = euclidean_distance((starting_node.x, starting_node.y, starting_node.z), (target_node.x, target_node.y, target_node.z))
    scalar = get_scalar(r2, start=starting_node.z, final=target_node.z)
    return get_energy_cost(r3, scalar)

def main():
    food_item_0 = FoodItem(food_id=0, x=0, y=0, z=0, energy=4)
    food_item_1 = FoodItem(food_id=1, x=1, y=2, z=-1, energy=3)
    food_item_2 = FoodItem(food_id=2, x=1, y=4, z=5, energy=5)
    food_item_3 = FoodItem(food_id=3, x=3, y=0, z=-2, energy=2)
    food_item_4 = FoodItem(food_id=4, x=-3, y=-2, z=4, energy=6)

    # calculate_all(node1 = food_item_0, node2 = food_item_3)

    print(valid_move(4, food_item_0, food_item_3))

main()
