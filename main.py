from Graph import Graph

if __name__ == "__main__":
    graph = Graph(
                seed=42069,
                visual_delay=0.5,
                starting_node_index=0,
                live_plot=False,
                path_printing=True, 
                optimal_update=False,
                input_file="test_cases_3.csv",
                output_file="solution.csv"
                )

    graph.run(num_points=6, 
        find_min=True,
        create_random_data=False, 
        starting_energy=1,
        max_energy=23,
        x_lower_limit=0, x_upper_limit=3,
        y_lower_limit=0, y_upper_limit=3,
        z_lower_limit=0, z_upper_limit=3,
        energy_lower_limit=10, energy_upper_limit=20,
        )
    