import pytest

if __name__ == "__main__":
    """
    This file is used to run all the tests in the test files. 
    Simply run this file to run all the tests.
    """
    # NOTE: list of command line args: ["-v" for verbose, <filename>.py to run specific test file]

    # Run the tests in test_food_item.py
    pytest.main(["-v", "test_food_item.py"])  
   
    # Run the tests in test_path.py
    pytest.main(["-v", "test_path.py"])
    
    # Run the tests in test_graph.py
    pytest.main(["-v", "test_graph.py"])