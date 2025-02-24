from Graph import Graph
from Data import Data

if __name__ == "__main__":
    # Set the starting node index (Default: 0)
    starting_node_index = 0

    # Set file path for reading data (Optional)
    node_data_to_read = "./random_coordinates_energy.csv"
    # node_data_to_read = "./memo_test_data.csv"

    # Create a Data object and generate random data
    data = Data()

    # Create a Graph object and read data from CSV
    graph = Graph()

    # Set visualization delay (Optional)
    data.visual_delay = 0.05

    # Generate random data and write to CSV
    data.create_random_data(4)

    # Read random data from CSV file
    graph.read_csv_data(node_data_to_read)

    # Initialize remaining food list from data
    graph.initialize_remaining_food()

    # Remove the starting node from the remaining food list
    graph.remaining_food.remove(0)
    
    # Add the starting node to the path
    graph.current_path.path_list.append(0)

    # Run solver with dynamic plotting
    graph.setup(data, 
                starting_energy=10, 
                max_energy=15,
                live_plot=False)

    # Print results and save solution
    graph.results_print()

    data.plot_solution()
    data.show_final_plot()
