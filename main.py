from Graph import Graph

if __name__ == "__main__":
    graph = Graph(
                seed=42069,
                visual_delay=0.001,
                starting_node_index=0,
                live_plot=False,
                path_printing=True, 
                optimal_update=False,
                input_file="test_cases_2.csv",
                output_file="solution.csv"
                )

    graph.run(num_points=5, 
        find_min=False,
        create_random_data=False, 
        starting_energy=21, 
        max_energy=25)
    