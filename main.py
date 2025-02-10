from Graph import Graph
from Food_Item import FoodItem
from copy import deepcopy
from calculation_tester import get_total_cost
import bisect

def solve(graph : Graph, node : FoodItem) -> None:

    print(f"Current Path: {graph.current_path}")
    print(f"Net Gain: {graph.current_path.net_energy_gain}")
    print()
    if(len(graph.remaining_food) == 0):
        print(f"Current Optimal: {graph.optimal_path}")
        print(f"Net Gain: {graph.optimal_path.net_energy_gain}")
        print()
        graph.update_optimal()

        return

    for food in graph.remaining_food:
        cost = get_total_cost(node, graph.all_food_nodes[food])

        if(graph.current_path.net_energy_gain >= cost):
            graph.remaining_food.remove(food)
            graph.current_path.path_list.append(food)
            graph.current_path.net_energy_gain -= cost

            solve(graph, graph.all_food_nodes[food])

            graph.current_path.net_energy_gain += cost
            graph.current_path.path_list.remove(food)
            bisect.insort(graph.remaining_food, food)
        
def main():
    graph = Graph()
    graph.read_csv_data("./random_coordinates_energy.csv")
    graph.initialize_remaining_food()
    graph.current_path.net_energy_gain = graph.all_food_nodes[0].energy
    starting_node = graph.all_food_nodes[0]
    graph.remaining_food.remove(0)
    graph.current_path.path_list.append(0)
    solve(graph, starting_node)
    print(f"optimal: {graph.optimal_path}")
    print(f"net: {graph.optimal_path.net_energy_gain}")

if __name__ == "__main__":
    main()



