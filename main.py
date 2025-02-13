from Graph import Graph
from Food_Item import FoodItem
from copy import deepcopy
from calculation_tester import get_total_cost
import bisect

def print_current_path(graph : Graph):
    print(f"Current Path: {graph.current_path}")
    print(f"Net Gain: {graph.current_path.net_energy_gain}")
    print()

def solve(graph : Graph, node : FoodItem) -> None:

    #print_current_path(graph)
    if(len(graph.remaining_food) == 0):
        graph.update_optimal()

        return

    for food in graph.remaining_food:
        cost = get_total_cost(node, graph.all_food_nodes[food])

        if(graph.current_path.net_energy_gain >= cost):
            graph.remaining_food.remove(food)
            graph.current_path.path_list.append(food)
            graph.current_path.net_energy_gain -= cost
            graph.current_path.net_energy_gain += graph.all_food_nodes[food].energy

            solve(graph, graph.all_food_nodes[food])
            graph.current_path.net_energy_gain -= graph.all_food_nodes[food].energy
            graph.current_path.net_energy_gain += cost
            graph.current_path.path_list.remove(food)
            bisect.insort(graph.remaining_food, food)
            #graph.remaining_food.push(food)
        #print_current_path(graph)

def min_starting_node(graph : Graph) -> FoodItem:
    for i in range(0, 1000):
        graph.current_path.net_energy_gain = i
        solve(graph, graph.all_food_nodes[0])
        if (graph.optimal_path.path_list):
            print(f"Found min: {i}")
            break

def main():
    graph = Graph()
    graph.read_csv_data("./random_coordinates_energy_modded.csv")
    graph.initialize_remaining_food()
    #graph.current_path.net_energy_gain = graph.all_food_nodes[0].energy
    #starting_node = graph.all_food_nodes[0]
    graph.remaining_food.remove(0)
    graph.current_path.path_list.append(0)
    min_starting_node(graph)
    #solve(graph, starting_node)
    print("done")
    print(f"optimal: {graph.optimal_path}")
    print(f"net: {graph.optimal_path.net_energy_gain}")
    graph.write_solution_to_csv("solution.csv")

if __name__ == "__main__":
    main()



