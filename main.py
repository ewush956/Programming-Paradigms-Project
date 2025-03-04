from Graph import Graph

TESTS_DIRECTORY = "./test_cases"
if __name__ == "__main__":
    graph = Graph(
                seed=42069,
                visual_delay=0.001,
                starting_node_index=0,
                live_plot=True,
                path_printing=False, 
                optimal_update=False,
                input_file=f"{TESTS_DIRECTORY}/1.csv",
                output_file="solution.csv"
                )

    graph.run(num_points=6, 
        find_min=True,
        create_random_data=False, 
        starting_energy=34,
        max_energy=36,
        x_lower_limit=0, x_upper_limit=3,
        y_lower_limit=0, y_upper_limit=3,
        z_lower_limit=0, z_upper_limit=3,
        energy_lower_limit=10, energy_upper_limit=20,
        )
