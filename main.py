# main.py
import bisect
import time

import matplotlib.pyplot as plt

from proj_math import get_total_cost
from Graph import Graph
from Data import Data


def solve(graph : Graph, node : int, data : Data, visual_delay : float = 0.001) -> None:
    """
    Recursively explores all possible paths starting from the given node.

    If there are no remaining food items, it updates the optimal path.
    Otherwise, for each food in the remaining list, if there is enough energy to reach it,
    the algorithm moves forward and then backtracks to explore other options.
    """
    if not graph.remaining_food:
        graph.update_optimal()
        return

    for food in list(graph.remaining_food):
        next_node = graph.all_food_nodes[food]
        cost = get_total_cost(node, next_node)

        if graph.current_path.net_energy_gain >= cost:
            # Move forward.
            graph.remaining_food.remove(food)
            graph.current_path.path_list.append(food)
            graph.current_path.net_energy_gain -= cost
            graph.current_path.net_energy_gain += next_node.energy

            # 🚀 **Live update the plot while solving (Optional) **🚀 (wooooosh... rockets!)
            data.update_plot(graph, solved=False)

            solve(graph, next_node, data)

            # Backtrack: undo changes to try another path.
            graph.current_path.net_energy_gain -= next_node.energy
            graph.current_path.net_energy_gain += cost
            graph.current_path.path_list.remove(food)
            bisect.insort(graph.remaining_food, food)

            # 🚀 **Live update during backtracking (Optional) **🚀  (wooooosh... more rockets!)
            data.update_plot(graph, solved=False)


def solver_find_min_energy(graph : Graph, data : Data, starting_energy: int = 1, max_energy: int = 1000) -> int:
    """
    Finds the minimum starting energy needed to complete a valid path.
    Iterates from starting_energy to max_energy until a valid path is found.
    """
    for energy in range(starting_energy, max_energy + 1):
        graph.current_path.net_energy_gain = energy
        solve(graph, graph.all_food_nodes[0], data)
        if graph.optimal_path.path_list:
            return energy
    return max_energy  # If no valid path is found, return max_energy.


def setup_solver(graph: Graph, data: Data, starting_energy : int = 1, max_energy : int = 1000) -> None:
    """
    Initializes the graph, computes the optimal path, and writes the solution to a CSV file.
    """
    print("Searching for optimal path 🔎 ...\n")
    
    # Start live plotting (Optional, need to ensure plotting in solve() is enabled)
    plt.ion()  # 🔴 **Enable interactive mode for live updates (ooooo emoji's)**
    
    # Start the timer and find the minimum starting energy.
    graph.solution_start_time = time.time()
    graph.min_energy_needed = solver_find_min_energy(graph, data, starting_energy=starting_energy, max_energy=max_energy)
    graph.solution_end_time = time.time()

    # Write the solution to a CSV file
    graph.write_solution_to_csv("solution.csv")


if __name__ == "__main__":
    # Set the starting node index, default is zero. (Optional)
    starting_node_index = 0

    # Set the file path to read the data from. (Optional)
    #node_data_to_read = "./random_coordinates_energy.csv"
    node_data_to_read = "./memo_test_data.csv"

    # 💾 Create a Data object and generate random data. Set the seed to a value for reproducibility.
    data = Data()

    # 📈 Create a Graph object and read the random data from the CSV file.
    graph = Graph()

    # Set the visual delay for the plot. (Optional)
    data.visual_delay = 0.0001

    # Generate random data and write it to a CSV file. Enter a value for the number of data points.
    data.create_random_data(4)

    # Read the random data from the CSV file.
    graph.read_csv_data(node_data_to_read)

    # Initialize the remaining food list from the data.
    graph.initialize_remaining_food()
    
    # Set up the starting conditions. Remove the starting node from the remaining food list.
    graph.remaining_food.remove(starting_node_index)

    # Add the starting node to the current path. 
    # NOTE: The starting node is always 0 to find the minimum energy needed.
    graph.current_path.path_list.append(starting_node_index)

    # Run the solver algorithm and dynamically update the plot.
    # The optimal path is stored in the graph object.
    # The solution is written to a CSV file which appear in order of the path taken.
    setup_solver(graph, data, starting_energy=10, max_energy=60)

    # Print results and write the solution to a CSV file.
    graph.results_print()

    # Update the final optimal path after solving (Optional, need to ensure plotting in solve() is enabled)
    data.update_plot(graph, solved=True)
    
    # Show the final plot (Optional, requires other plotting functions to be enabled)
    data.show_final_plot()

    # Show the solution plot with additional information. (Optional)
    data.plot_solution()
