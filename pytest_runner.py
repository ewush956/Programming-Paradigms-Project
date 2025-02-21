import pytest

if __name__ == "__main__":
    pytest.main(["-v", "test_food_item.py"])  # list of command line args: ["-v" for verbose, <filename>.py to run spoecific test file]
    pytest.main(["-v", "test_path.py"])  # list of command line args: ["-v" for verbose, <filename>.py to run spoecific test file]
    pytest.main(["-v", "test_graph.py"])  # list of command line args: ["-v" for verbose, <filename>.py to run spoecific test file]