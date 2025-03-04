from Graph import Graph

TESTS_DIRECTORY = "./test_cases"

if __name__ == "__main__":
    graph = Graph(
                seed=42069,
                visual_delay=0.05,
                starting_node_index=0,
                path_printing=False,
                optimal_update=False,
                path_update=False,
                input_file=f"{TESTS_DIRECTORY}/2.csv",
                output_file="solution.csv"
                )

    graph.run(num_points=6, 
        find_min=True,
        create_random_data=False, 
        starting_energy=1,
        max_energy=50,
        x_lower_limit=0, x_upper_limit=3,
        y_lower_limit=0, y_upper_limit=3,
        z_lower_limit=0, z_upper_limit=3,
        energy_lower_limit=1, energy_upper_limit=3,
        )

