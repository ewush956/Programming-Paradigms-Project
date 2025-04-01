### Dependancies 
run `pip install matplotlib` For live plotting and final graph.
run `pip install pytest` For running the test driver.

### How to run the program
run `python .\main.py` after installing required dependancies either locally or in a virtual environment.

### Command-Line Arguments
The program accepts the following command-line arguments to customize its behavior:

- `--input_file` (str, default: "1.csv"): Input file name located in the `test_cases` directory.
- `--output_file` (str, default: "solution.csv"): Output file name for saving results.
- `--live_plot` (flag, default: False): Enable live plotting during execution.
- `--show_final_graph` (flag, default: False): Display the final graph after execution.
- `--path_printing` (flag, default: False): Print the path taken during execution.
- `--optimal_update` (flag, default: False): Enable optimal updates for the algorithm.
- `--seed` (int, default: 12345): Seed for random number generation.
- `--visual_delay` (float, default: 0.0001): Delay in seconds for visual updates.
- `--starting_node_index` (int, default: 0): Index of the starting node.
- `--num_points` (int, default: 6): Number of points to process.
- `--find_min` (flag, default: False): Enable finding the minimum value.
- `--create_random_data` (flag, default: False): Generate random data for testing.
- `--starting_energy` (int, default: 1): Initial energy level.
- `--max_energy` (int, default: 100): Maximum energy level.
- `--x_lower_limit` (int, default: 0): Lower limit for x-coordinate.
- `--x_upper_limit` (int, default: 3): Upper limit for x-coordinate.
- `--y_lower_limit` (int, default: 0): Lower limit for y-coordinate.
- `--y_upper_limit` (int, default: 3): Upper limit for y-coordinate.
- `--z_lower_limit` (int, default: 0): Lower limit for z-coordinate.
- `--z_upper_limit` (int, default: 3): Upper limit for z-coordinate.
- `--energy_lower_limit` (int, default: 10): Lower limit for energy values.
- `--energy_upper_limit` (int, default: 20): Upper limit for energy values.

### Example Usage
```bash
python ./main.py --seed 42 --live_plot --input_file example.csv --num_points 10
```




