from Graph import Graph
from Food_Item import FoodItem
from Data import Data
from proj_math import get_total_cost
import matplotlib.pyplot as plt
import bisect
import time

plt.ion()

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')

def update_plot(graph, solved : bool, pause_timer : float = 0.001) -> None:
    ax.clear()
    # Plot all nodes (assuming each FoodItem has x, y, z attributes)
    all_nodes = list(graph.all_food_nodes)
    x_all = [node.x for node in all_nodes]
    y_all = [node.y for node in all_nodes]
    z_all = [node.z for node in all_nodes]
    ax.scatter(x_all, y_all, z_all, c='purple', alpha=0.5)

    # Plot current path in red
    if graph.current_path.path_list:
        path_nodes = [graph.all_food_nodes[node] for node in graph.current_path.path_list]
        if (solved) :
            path_nodes = [graph.all_food_nodes[node] for node in graph.optimal_path.path_list]
        path_x = [node.x for node in path_nodes]
        path_y = [node.y for node in path_nodes]
        path_z = [node.z for node in path_nodes]
        ax.plot(path_x, path_y, path_z, color='purple', marker='o')

    plt.draw()
    plt.pause(pause_timer)


def solve(graph: Graph, node: FoodItem) -> None:
    """
    Recursively explores all possible paths starting from the given node.

    If there are no remaining food items, it updates the optimal path.
    Otherwise, for each food in the remaining list, if there is enough energy to reach it,
    the algorithm moves forward and then backtracks to explore other options.
    """
    #print_current_path(graph)
    if not graph.remaining_food:
        graph.update_optimal()
        return

    # Iterate over a copy of the list to allow modifications during iteration.
    for food in graph.remaining_food:
        next_node = graph.all_food_nodes[food]
        cost = get_total_cost(node, next_node)

        if graph.current_path.net_energy_gain >= cost:
            # Move forward: choose this food item.
            graph.remaining_food.remove(food)
            graph.current_path.path_list.append(food)
            graph.current_path.net_energy_gain -= cost
            graph.current_path.net_energy_gain += next_node.energy
            
            update_plot(graph, False, 0.001)
            # Recursively explore from the new node.
            solve(graph, next_node)
            
            # Backtrack: undo the changes to try another path.
            graph.current_path.net_energy_gain -= next_node.energy
            graph.current_path.net_energy_gain += cost
            graph.current_path.path_list.remove(food)
            bisect.insort(graph.remaining_food, food)

            update_plot(graph, False, 0.001)
        #print_current_path(graph)


def min_starting_energy(graph: Graph, starting_energy = 61, max_energy: int = 1000) -> int:
    """
    Finds the minimum starting energy needed to complete a valid path.

    Iterates through energy values from 0 to max_energy until a valid path is found.
    Returns the first energy value that results in a valid path.
    """
    for energy in range(starting_energy, max_energy + 1):
        # print(f"Attempting to find optimal route with {energy} starting energy\n")
        graph.current_path.net_energy_gain = energy
        solve(graph, graph.all_food_nodes[0])
        if graph.optimal_path.path_list:
            return energy
    return max_energy  # Return max_energy if no valid path is found


def run() -> None:
    """Initializes the graph, computes the optimal path, and writes the solution to a CSV file."""
    
    # Initialize a graph object and read the CSV data.
    graph = Graph()
    
    # Read the CSV data.
    graph.read_csv_data("./random_coordinates_energy.csv")
    
    # Initialize the remaining food list.
    graph.initialize_remaining_food()
    
    # Remove the starting node from the remaining food list.
    graph.remaining_food.remove(0)
    
    # Add the starting node to the current path.
    graph.current_path.path_list.append(0)
    
    # Print the initial state of the graph.
    print("Searching for optimal path...\n")
    
    # Start the timer and compute the optimal path.
    graph.solution_start_time = time.time()
    
    # Find the minimum starting energy needed to complete the path.
    graph.min_energy_needed = min_starting_energy(graph, starting_energy=61, max_energy=1000)
    
    # End the timer.
    graph.solution_end_time = time.time()
    
    # Update the plot with the optimal path.
    update_plot(graph, True)
    
    # Turn off interactive mode to keep the plot open.
    plt.ioff()
    
    # Plot the optimal path.
    plt.show()
    
    # Print the results of the search.
    graph.results_print(graph)
    
    # Write the optimal path to a CSV file.
    graph.write_solution_to_csv("solution.csv")

if __name__ == "__main__":
    data = Data()
    data.create_random_data()
    run()
