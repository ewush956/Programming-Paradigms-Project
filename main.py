from graph import Graph
from path import Path
from food_item import FoodItem
import math

def solve(graph : Graph) -> bool:
    """
    optimalP = null

    def solve(p: Problem):
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
    graph.read_csv_data("random_coordinates_energy.csv")

    for food in graph.food_items:
        print(food.food_id)

if __name__ == "__main__":
    main()



