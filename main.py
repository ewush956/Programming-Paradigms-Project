from graph import Graph

if __name__ == "__main__":
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
    graph = Graph(
                seed=420,
                starting_node_index=0,
                live_plot=False,
                path_printing=False, 
                optimal_update=False,
                # input_file="<choose_file>.csv",
                # output_file="<choose_file>.csv"
                )

    """ Manually set the visual delay for plotting the graph (Optional, default is 0.005) """
    # graph.data.visual_delay = 0.01
    
    """
    Generate random data and write to CSV.
    The number of points should be at least 3 more than the starting node 
    index to form a decent graph path.
    """
    graph.data.create_random_data(num_points=8,
                                  x_lower_limit=0, x_upper_limit=10,
                                  y_lower_limit=0, y_upper_limit=10,
                                  z_lower_limit=0, z_upper_limit=4,
                                  energy_lower_limit=1, energy_upper_limit=5)

    """ Read random data from default CSV file or user specified file """
    graph.read_csv_data(filename=None)
    
    """ Initialize remaining food list from data """
    graph.initialize_remaining_food()
    
    if graph.is_valid_starting_node():
      
      """
      Run the graph setup with the starting energy, max energy, 
      and find_min set to the user choice (or Default). find_min set to True 
      will find the minimum energy path required for one solution (if possible 
      within the constraints). Else if set to False it will use the starting 
      energy to attempt to find a path.
      """
      graph.setup_solver(starting_energy=1, max_energy=30, find_min=True)

      """
      Write the solution to CSV, print results and plot the solution
      Use default output file or user specified file in write_solution_to_csv
      """
      graph.write_solution_to_csv(filename=None)
      graph.results_print()
      graph.data.plot_solution()
      graph.data.show_final_plot()
    
    else:
        """ Print error message if the starting node index is invalid """
        print(
          f"Invalid starting node index choice: {graph.starting_node_index}.\n"
          f"List of valid indices: {graph.remaining_food}\n"
          )
