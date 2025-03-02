from graph import Graph

if __name__ == "__main__":
    graph = Graph(
                seed=42068,
                visual_delay=0.005,
                starting_node_index=5,
                live_plot=False,
                path_printing=False, 
                optimal_update=False,
                input_file="random_coordinates_energy.csv",
                output_file="solution.csv"
                )
    
    graph.run(num_points=7, 
        find_min=True, 
        create_random_data=True, 
        starting_energy=1, 
        max_energy=25)
    