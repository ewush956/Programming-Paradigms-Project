from Graph import Graph

TESTS_DIRECTORY = "./test_cases"
if __name__ == "__main__":
    graph = Graph(
                seed=81285,
                visual_delay=0.00,
                starting_node_index=0,
                live_plot=False,
                path_printing=False, 
                optimal_update=True,
                path_update=False,
                #input_file=f"{TESTS_DIRECTORY}/5.csv",
                output_file="solution.csv"
                )

    graph.run(num_points=12, 
        find_min=True,
        create_random_data=True, 
        starting_energy=1,
        max_energy=50,
        x_lower_limit=0, x_upper_limit=3,
        y_lower_limit=0, y_upper_limit=3,
        z_lower_limit=0, z_upper_limit=3,
        energy_lower_limit=1, energy_upper_limit=5,
        )
