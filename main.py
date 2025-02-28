from Graph import Graph

if __name__ == "__main__":
    graph = Graph(seed=42, 
                starting_node_index=1,
                live_plot=True, 
                path_printing=False, 
                optimal_update=True,
                input_file="random_coordinates_energy2.csv",
                output_file="solution2.csv"
                )
    """
    ==================== Creating a Graph object ====================

    - Set the seed for random number generation for reproducibility (Optional).

    - You can set the starting node index of the graph (Optional, default is 0).

    - Set live_plot to True if you want to see the solution path 
      in real-time (Optional, default is False).

    - Set path_printing to True if you want to print the path to 
      the console (Optional, default is False).

    - Set optimal_update to True if you want to print the current optimal 
      path when it is updated (Optional, default is False).

    - Set input_file to the filename of the CSV file containing the data 
    (Optional, default is "random_coordinates_energy.csv").

    - Set output_file to the filename of the CSV file to write the solution to 
    (Optional, default is "solution.csv").
    """

    # Set the visual delay for plotting the graph (Optional, default is 0.005)
    # graph.data.visual_delay = 0.01
    
    # Generate random data and write to CSV.
    # The number of points should be at least 3 more than the starting node 
    # index to avoid index out of range errors and to form a graph path.
    graph.data.create_random_data(num_points=4)

    # Read random data from CSV file
    graph.read_csv_data()

    # Initialize remaining food list from data
    graph.initialize_remaining_food()

    # Remove the chosen starting node from the remaining food list
    if graph.starting_node_index in graph.remaining_food:

        # Remove the starting node from the remaining food list
        graph.remaining_food.remove(graph.starting_node_index)
        
        # Add the starting node to the path
        graph.current_path.path_list.append(graph.starting_node_index)
        
        # Run solver with dynamic plotting, with bounds on starting energy and max energy
        graph.setup(starting_energy=1, 
                    max_energy=50)

        # Write the solution to a CSV file
        graph.write_solution_to_csv()

        # Print results to the console
        graph.results_print()

        # Plot the solution path to the graph
        graph.data.plot_solution()

        # Show the final plot of the solution
        graph.data.show_final_plot()
        
    else:
        # Print error message if the starting node index is invalid
        print(f"Invalid starting node index: {graph.starting_node_index}")
