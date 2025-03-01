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
                live_plot=True,
                path_printing=False, 
                optimal_update=False,
                # input_file="test_cases_1.csv",
                # output_file="solution_test_case1.csv"
                )

    graph.run(num_points=5, 
        find_min=False, 
        create_random_data=True, 
        starting_energy=50, 
        max_energy=50)
