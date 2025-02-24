from Graph import Graph

if __name__ == "__main__":
    # Create a Graph object and read data from CSV.
    # Set the seed for random number generation for reproducibility.
    # You can set the starting node index here (Optional, default is 0).
    graph = Graph(seed=123, live_plot=True, starting_node_index=0)

    # Set file path for reading data (Optional)
    node_data_to_read = "./random_coordinates_energy.csv"
    # node_data_to_read = "./memo_test_data.csv"

    # Set visualization delay (Optional)
    # graph.data.visual_delay = 0.05

    # Generate random data and write to CSV
    graph.data.create_random_data(6)

    # Read random data from CSV file
    graph.read_csv_data(node_data_to_read)

    # Initialize remaining food list from data
    graph.initialize_remaining_food()

    # Remove the chosen starting node from the remaining food list
    if graph.starting_node_index in graph.remaining_food:
        # Remove the starting node from the remaining food list
        graph.remaining_food.remove(graph.starting_node_index)
        
        # Add the starting node to the path
        graph.current_path.path_list.append(graph.starting_node_index)
        
        # Run solver with dynamic plotting
        graph.setup(starting_energy=20, max_energy=26)

        # Print results and save solution
        graph.results_print()

        # Plot the solution path to the graph
        graph.data.plot_solution()

        # Show the final plot of the solution
        graph.data.show_final_plot()

    else:
        print(f"Invalid starting node index: {graph.starting_node_index}")
