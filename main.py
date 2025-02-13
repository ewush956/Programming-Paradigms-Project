from Graph import Graph
from Food_Item import FoodItem
from proj_math import get_total_cost
import bisect
import time

def print_current_path(graph: Graph) -> None:
    """Prints the current path and net energy gain."""
    print(f"Current Path: {graph.current_path}")
    print(f"Net Gain: {graph.current_path.net_energy_gain}\n")

def solve(graph: Graph, node: FoodItem) -> None:
    """
    Recursively explores all possible paths starting from the given node.

    If there are no remaining food items, it updates the optimal path.
    Otherwise, for each food in the remaining list, if there is enough energy to reach it,
    the algorithm moves forward and then backtracks to explore other options.
    """
    if not graph.remaining_food:
        graph.update_optimal()
        return

    # Iterate over a copy of the list to allow modifications during iteration.
    for food in list(graph.remaining_food):
        next_node = graph.all_food_nodes[food]
        cost = get_total_cost(node, next_node)

        if graph.current_path.net_energy_gain >= cost:
            # Move forward: choose this food item.
            graph.remaining_food.remove(food)
            graph.current_path.path_list.append(food)
            graph.current_path.net_energy_gain -= cost
            graph.current_path.net_energy_gain += next_node.energy
            
            # Recursively explore from the new node.
            solve(graph, next_node)
            
            # Backtrack: undo the changes to try another path.
            graph.current_path.net_energy_gain -= next_node.energy
            graph.current_path.net_energy_gain += cost
            graph.current_path.path_list.remove(food)
            bisect.insort(graph.remaining_food, food)

def min_starting_energy(graph: Graph, max_energy: int = 1000) -> int:
    """
    Finds the minimum starting energy needed to complete a valid path.

    Iterates through energy values from 0 to max_energy until a valid path is found.
    Returns the first energy value that results in a valid path.
    """
    for energy in range(max_energy):
        graph.current_path.net_energy_gain = energy
        solve(graph, graph.all_food_nodes[0])
        if graph.optimal_path.path_list:
            return energy
    return max_energy  # Return max_energy if no valid path is found

def main() -> None:
    """Initializes the graph, computes the optimal path, and writes the solution to a CSV file."""
    graph = Graph()
    graph.read_csv_data("./random_coordinates_energy.csv")
    graph.initialize_remaining_food()
    
    # Initialize starting conditions using food item 0.
    graph.remaining_food.remove(0)
    graph.current_path.path_list.append(0)
    
    print("Searching for optimal path...\n")
    start_time = time.time()
    min_energy_needed = min_starting_energy(graph)
    end_time = time.time()

    print(f"Done! Finished in {end_time - start_time:.6f} seconds\n")
    print(f"Minimum Starting Energy Needed To Finish: {min_energy_needed}\n")
    print(f"Optimal Path: {graph.optimal_path} --- Finished Optimal Net Energy: {graph.optimal_path.net_energy_gain}\n")

    graph.write_solution_to_csv("solution.csv")

if __name__ == "__main__":
    main()
