from Graph import Graph
from Food_Item import FoodItem
from copy import deepcopy
from proj_math import get_total_cost
import bisect
import time

def print_current_path(graph: Graph) -> None:
    """Prints the current path and net energy gain."""
    print(f"Current Path: {graph.current_path}")
    print(f"Net Gain: {graph.current_path.net_energy_gain}\n")

def solve(graph : Graph, node : FoodItem) -> None:
    #print_current_path(graph)
    if(len(graph.remaining_food) == 0):
        graph.update_optimal()
        return

    for food in graph.remaining_food:
        cost = get_total_cost(node, graph.all_food_nodes[food])

        if(graph.current_path.net_energy_gain >= cost):
            # Progressing forward
            graph.remaining_food.remove(food)
            graph.current_path.path_list.append(food)
            graph.current_path.net_energy_gain -= cost
            graph.current_path.net_energy_gain += graph.all_food_nodes[food].energy
            
            # Attempt to solve from new available node
            solve(graph, graph.all_food_nodes[food])

            # Backtrack to check other options
            graph.current_path.net_energy_gain -= graph.all_food_nodes[food].energy
            graph.current_path.net_energy_gain += cost
            graph.current_path.path_list.remove(food)
            bisect.insort(graph.remaining_food, food)


def min_starting_node(graph : Graph) -> FoodItem:
    for i in range(0, 1000):
        graph.current_path.net_energy_gain = i
        solve(graph, graph.all_food_nodes[0])
        if (graph.optimal_path.path_list):
            break
    return i

def main():
    graph = Graph()
    graph.read_csv_data("./random_coordinates_energy_modded.csv")
    graph.initialize_remaining_food()
    # graph.current_path.net_energy_gain = graph.all_food_nodes[0].energy
    # starting_node = graph.all_food_nodes[0]
    graph.remaining_food.remove(0)
    graph.current_path.path_list.append(0)
    print("Searching for optimal path...\n")
    start_time = time.time()
    min_energy_needed = min_starting_node(graph)
    # solve(graph, starting_node)
    end_time = time.time()
    print(f"Done! Finished in {end_time - start_time:.6f} seconds\n")
    print(f"Optimal Path: {graph.optimal_path}\n")
    print(f"Minimum Starting Energy Needed To Finish: {min_energy_needed}\n")
    print(f"Finished Net Energy: {graph.optimal_path.net_energy_gain}\n")
    graph.write_solution_to_csv("solution.csv")

if __name__ == "__main__":
    main()



