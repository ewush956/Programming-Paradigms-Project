import pytest

from Path import Path
from Food_Item import FoodItem

def test_path_creation():
    """Test FoodItem creation."""
    path_tester = Path()
    empty_food_item = FoodItem(None, None, None, None, None)
    assert path_tester.current_food_node == empty_food_item
    assert path_tester.path_list == []
    assert path_tester.net_energy_gain == 0

def test_path_appending():
    """Test FoodItem appending."""
    path_tester = Path()
    food_item = FoodItem(0, 1, 2, 3, 4)
    path_tester.path_list.append(food_item.food_id)
    path_tester.current_food_node = food_item
    assert path_tester.path_list[0] == 0
    assert path_tester.current_food_node == food_item
    assert len(path_tester.path_list) == 1

def test_path_energy():
    path_tester = Path()
    assert path_tester.net_energy_gain == 0
    path_tester.net_energy_gain += 10
    assert path_tester.net_energy_gain == 10
    path_tester.net_energy_gain -= 5
    assert path_tester.net_energy_gain == 5