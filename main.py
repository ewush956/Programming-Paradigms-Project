from graph import Graph
from path import Path
from food_item import FoodItem
import math

def solve(graph : Graph) -> bool:
    if(len(graph.remaining_food) == 0):
        graph.update_optimal()
        return False
    else:
        for food_id in graph.remaining_food:
            graph.current_path.current_food = food_id
    
    """
    if p is solved:
        optimalP = get_optimal(optimalP, p)   
        set p to not solved
    for each move in possible moves for p:
        apply move to p to get p'
        solve(p')
        undo move  # backtrack
    return optimalP
    """
    pass

def main():
    graph = Graph()
    graph.remaining_food = [1,2,3,4]

    graph.current_path.path_list = [1,2,3]
    graph.optimal_path.path_list = []

    graph.current_path.net_energy_gain = 0
    graph.optimal_path.net_energy_gain = 0

    solve(graph)

if __name__ == "__main__":
    main()



