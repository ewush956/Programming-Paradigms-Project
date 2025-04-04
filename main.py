import argparse
from Graph import Graph

TESTS_DIRECTORY = "./test_cases"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--visual_delay", type=float, default=0.0001)
    parser.add_argument("--starting_node_index", type=int, default=0)
    parser.add_argument("--live_plot", action="store_true", default=False)
    parser.add_argument("--show_final_graph", action="store_true", default=False)
    parser.add_argument("--path_printing", action="store_true", default=False)
    parser.add_argument("--optimal_update", action="store_true", default=False)
    parser.add_argument("--input_file", type=str, default='',
                        help="Filename located in the test_cases directory")
    parser.add_argument("--output_file", type=str, default="solution.csv")
    parser.add_argument("--num_points", type=int, default=6)
    parser.add_argument("--find_min", action="store_true", default=False)
    parser.add_argument("--create_random_data", action="store_true", default=False)
    parser.add_argument("--starting_energy", type=int, default=1)
    parser.add_argument("--max_energy", type=int, default=100)
    parser.add_argument("--x_lower_limit", type=int, default=0)
    parser.add_argument("--x_upper_limit", type=int, default=3)
    parser.add_argument("--y_lower_limit", type=int, default=0)
    parser.add_argument("--y_upper_limit", type=int, default=3)
    parser.add_argument("--z_lower_limit", type=int, default=0)
    parser.add_argument("--z_upper_limit", type=int, default=3)
    parser.add_argument("--energy_lower_limit", type=int, default=10)
    parser.add_argument("--energy_upper_limit", type=int, default=20)

    args = parser.parse_args()

    graph = Graph(
        seed=args.seed,
        visual_delay=args.visual_delay,
        starting_node_index=args.starting_node_index,
        live_plot=args.live_plot,
        show_final_graph=args.show_final_graph,
        path_printing=args.path_printing,
        optimal_update=args.optimal_update,
        input_file=args.input_file,
        output_file=args.output_file
    )
    if not args.live_plot:
        args.visual_delay = 0

    if args.create_random_data:
        args.input_file = "create_random_data.csv"

    if args.input_file == '' and not args.create_random_data:
        print("\nNo File specified, provide a file directory")
        print(r'python .\main.py --input_file ".\test_cases\file_name.csv" ')
        print("or use --create_random_data to generate random data\n")
        graph.valid = False
    try: 
        if graph.valid:
            graph.run(
                num_points=args.num_points,
                find_min=args.find_min,
                create_random_data=args.create_random_data,
                starting_energy=args.starting_energy,
                max_energy=args.max_energy,
                x_lower_limit=args.x_lower_limit,
                x_upper_limit=args.x_upper_limit,
                y_lower_limit=args.y_lower_limit,
                y_upper_limit=args.y_upper_limit,
                z_lower_limit=args.z_lower_limit,
                z_upper_limit=args.z_upper_limit,
                energy_lower_limit=args.energy_lower_limit,
                energy_upper_limit=args.energy_upper_limit,
            )
    except FileNotFoundError as e:
        print("Error: Invalid file path provided.", e)
    
if __name__ == "__main__":
    main()

