## Overview of the Problem

This project implements a **pathfinding algorithm** where the traversal between nodes is constrained by **available energy**. The nodes are represented in a 3D cartesian space, and the cost of moving between nodes is determined by a combination of:
- **Euclidean distance** between nodes.
- A **gradient scalar** based on the z-axis difference constrained between the values on the open interval (0,2).

The goal is to find valid paths through the graph, ensuring that the energy constraints are met. The program can handle cases with:
- No solutions.
- One solution.
- Multiple solutions.
- Invalid User input.

### Dependancies 
Install `pip` on your machine if you have not already done so.
run `pip install matplotlib` For live plotting and final graph.
run `pip install pytest` (Only for running the test driver.)

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

### Project Governance

This project was developed following a structured approach, with detailed documentation to ensure clarity and consistency throughout the process. Below are the key resources:

- **Development Plan**: A comprehensive plan outlining the steps and milestones for the project's implementation.  
  [View the Development Plan](Documentation/DevelopmentPlan.md)

- **Testing Plan**: A detailed plan describing the testing strategies, test cases, and expected outcomes to ensure the program's correctness and reliability.  
  [View the Testing Plan](Documentation/test_cases_info.md)

- **Weekly Log**: An informal log documenting weekly progress, challenges, and decisions made during the development process.  
  [View the Weekly Log](Documentation/WeeklyLogs.md)



