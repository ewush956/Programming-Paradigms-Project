from Food_Item import FoodItem
from math import sqrt

def euclidean_distance_r2(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def get_scalar(dist_r2, z1, z2):
    return (1 + ((z2 - z1) / dist_r2))

def euclidean_distance_r3(x1, y1, z1, x2, y2, z2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def get_energy_cost(dist_r3, scalar):
    return dist_r3 * scalar

def valid_move(net_energy : float, node1 : FoodItem, node2 : FoodItem):
    r2 = euclidean_distance_r2(x1=node1[1],y1=node1[2], x2=node2[1], y2=node2[2])
    r3 = euclidean_distance_r3(x1=node1[1],y1=node1[2], z1=node1[3], x2=node2[1], y2=node2[2], z2=node2[3])
    scalar = get_scalar(r2, z1=node1[3], z2=node2[3])
