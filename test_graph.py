import pytest
import os

from Graph import Graph
from Food import FoodItem
from Path import Path
from Data import Data


# Test the Graph class default initialization method to ensure it initializes correctly.
def test_graph_default_initialization():
    """Ensure Graph initializes correctly with empty attributes."""
    graph = Graph()
    assert isinstance(graph.optimal_path, Path)
    assert isinstance(graph.current_path, Path)
    assert isinstance(graph.data, Data)
    assert isinstance(graph.remaining_food, list)
    assert isinstance(graph.all_food_nodes, list)
    assert graph.min_energy_needed == 0
    assert graph.solution_start_time == 0
    assert graph.solution_end_time == 0
    assert graph.live_plot == False
    assert graph.path_printing == False
    assert graph.optimal_update == False
    assert graph.starting_node_index == 0
    assert graph.data.input_data_file == "random_coordinates_energy.csv"
    assert graph.data.output_data_file == "solution.csv"

# Test the Graph class custom initialization method to ensure it initializes correctly.
def test_graph_custom_initialization():
    """Ensure Graph initializes correctly with custom attributes."""
    graph = Graph(seed=123,
                  starting_node_index=1,
                  live_plot=True,
                  path_printing=True,
                  optimal_update=True,
                  input_file="test_data.csv",
                  output_file="test_solution.csv")
    assert isinstance(graph.optimal_path, Path)
    assert isinstance(graph.current_path, Path)
    assert isinstance(graph.data, Data)
    assert isinstance(graph.remaining_food, list)
    assert isinstance(graph.all_food_nodes, list)
    assert graph.min_energy_needed == 0
    assert graph.solution_start_time == 0
    assert graph.solution_end_time == 0
    assert graph.live_plot == True
    assert graph.path_printing == True
    assert graph.optimal_update == True
    assert graph.starting_node_index == 1
    assert graph.data.input_data_file == "test_data.csv"
    assert graph.data.output_data_file == "test_solution.csv"

# Test the Graph class read_csv_data method to ensure 
# it reads CSV data correctly.
def test_read_csv_data_valid(tmp_path):

    # Define the CSV header for the CSV file
    csv_header = "Node Number,X,Y,Z,Energy"
    
    # Create a temporary CSV file to store the sample data for testing where
    # tmp_path is the temporary directory used by pytest to store temporary files.
    csv_file = tmp_path / "test_data.csv"

    # Create sample data for testing and changes are reflected in the entire test
    item1 = (0, 10.0, 20.0, 30.0, 60)
    item2 = (1, 15.0, 25.0, 35.0, 45)
    
    # Correctly format CSV content using f-strings
    csv_content = f"{csv_header}\n" \
                  f"{item1[0]},{item1[1]},{item1[2]},{item1[3]},{item1[4]}\n" \
                  f"{item2[0]},{item2[1]},{item2[2]},{item2[3]},{item2[4]}\n"

    # Write sample CSV data
    csv_file.write_text(csv_content)
    
    # Initialize the Graph class. The first test passing ensures this works.
    graph = Graph(input_file=csv_file)
    
    # Use the read_csv_data method to read the CSV data.
    graph.read_csv_data()
    
    # Check that the CSV data was read correctly
    assert len(graph.all_food_nodes) == 2

    # Check that the FoodItem objects were created correctly 
    assert graph.all_food_nodes[0] == FoodItem(*item1)
    
    # Check that the FoodItem objects were created correctly
    assert graph.all_food_nodes[1] == FoodItem(*item2)


# Test the Graph class write_solution_to_csv method to ensure it writes the 
# optimal path to a CSV file correctly.
def test_write_solution_to_csv(tmp_path):
    """Ensure writing to CSV correctly exports the optimal path."""
    
    # Define the CSV header for the CSV file
    csv_header = "Node Number,X,Y,Z,Energy"
    
    # Add the sample data to the optimal path list where tmp_path is the
    # temporary directory used by pytest to store temporary files.
    csv_file = tmp_path / "solution.csv"

    # Create sample data for testing and changes are reflected in the entire test
    item0 = FoodItem(0, 10.0, 20.0, 30.0, 40)
    item1 = FoodItem(1, 15.0, 25.0, 35.0, 45)

    # Initialize the Graph class. The first test passing ensures this works.
    graph = Graph(output_file=csv_file)

    # Add FoodItems to all_food_nodes for csv writing
    graph.all_food_nodes = [item0, item1]

    # Write sample CSV data to the optimal path list where the optimal path
    # list is a list of node numbers. In this hypothetical case, the optimal
    # path list is [1, 0].
    graph.optimal_path.path_list = [1,0]
    
    # Use the write_solution_to_csv method to write the optimal path to a CSV file.
    graph.write_solution_to_csv()
    
    # Read the output file using the read_text method from the Pathlib module
    # and store the content in the content variable.
    content = csv_file.read_text()

    # Correctly format CSV content using f-strings
    # The expected content is the CSV header followed by the data for the two
    # FoodItems in the optimal path list. The data is formatted as a string.
    # NOTE: The optimal path path_list (above) in the graph is the order the csv 
    # will be written in.
    # Food Item 1 first followed by Food Item 0. This is why the path_list is [1,0]
    # Changing the order of the path_list without changing this string will cause
    # the test to fail.
    csv_expected_content = f"{csv_header}\n" \
                  f"{item1.food_id},{item1.x},{item1.y},{item1.z},{item1.energy}\n" \
                  f"{item0.food_id},{item0.x},{item0.y},{item0.z},{item0.energy}\n"

    
    # Check that the CSV data was written correctly by comparing the content
    # of the CSV file to the expected content. Uses the strip method to remove
    # any leading or trailing whitespace
    assert content.strip() == csv_expected_content.strip()
