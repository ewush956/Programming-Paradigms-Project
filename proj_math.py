from math import sqrt
from math import tanh

from Food_Item import FoodItem


def euclidean_distance(p1 : tuple, p2 : tuple):
    return sqrt(sum((a - b)**2 for a, b in zip(p1, p2)))

def get_scalar(dist_r2 : float, start : int, final : int) -> float:
    return (1 + (tanh(0.1*(final - start))))

def get_energy_cost(dist_r3 : float, scalar : float):
    return dist_r3 * scalar

def get_total_cost(starting_node : FoodItem, target_node : FoodItem) -> int:
    r2 = euclidean_distance((starting_node.x,starting_node.y), (target_node.x, target_node.y))
    r3 = euclidean_distance((starting_node.x, starting_node.y, starting_node.z), (target_node.x, target_node.y, target_node.z))
    scalar = get_scalar(r2, start=starting_node.z, final=target_node.z)
    return get_energy_cost(r3, scalar)
