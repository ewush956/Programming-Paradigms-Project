from Graph import Graph

if __name__ == "__main__":
    # Set the starting node index (Default: 0)
    starting_node_index = 0

    # Create a Graph object and read data from CSV
    graph = Graph()

    # Set file path for reading data (Optional)
    node_data_to_read = "./random_coordinates_energy.csv"
    # node_data_to_read = "./memo_test_data.csv"

    # Set visualization delay (Optional)
    graph.data.visual_delay = 0.05

    # Generate random data and write to CSV
    graph.data.create_random_data(4)

    # Enable live plotting (Optional)
    graph.live_plot = True

    # Read random data from CSV file
    graph.read_csv_data(node_data_to_read)

    # Initialize remaining food list from data
    graph.initialize_remaining_food()

    # Remove the starting node from the remaining food list
    graph.remaining_food.remove(0)
    
    # Add the starting node to the path
    graph.current_path.path_list.append(0)

    # Run solver with dynamic plotting
    graph.setup(starting_energy=20, max_energy=100,)

    # Print results and save solution
    graph.results_print()

    # Plot the solution path to the graph
    graph.data.plot_solution()

    # Show the final plot of the solution
    graph.data.show_final_plot()
