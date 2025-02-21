import pytest

from food_item import FoodItem


def test_food_item_creation_integers_positive():
    """Test FoodItem creation."""
    food_item = FoodItem(food_id=1, x=2, y=3, z=4, energy=5)
    assert food_item.food_id == 1
    assert food_item.x == 2
    assert food_item.y == 3
    assert food_item.z == 4
    assert food_item.energy == 5

    
def test_food_item_str_integers():
    item = FoodItem(food_id=1, x=2, y=3, z=4, energy=5)
    expected_output = "Food Id:1\nX-Coord:2\nY-Coord:3\nZ-Coord:4\nEnergy:5\n"
    assert str(item) == expected_output

    
def test_food_item_creation_floats():
    """Test FoodItem creation."""
    food_item = FoodItem(food_id=1, x=2.1, y=3.2, z=4.3, energy=5)
    assert food_item.food_id == 1
    assert food_item.x == 2.1
    assert food_item.y == 3.2
    assert food_item.z == 4.3
    assert food_item.energy == 5
    

def test_food_item_str_floats():
    item = FoodItem(food_id=1, x=2.1, y=3.2, z=4.3, energy=5)
    expected_output = "Food Id:1\nX-Coord:2.1\nY-Coord:3.2\nZ-Coord:4.3\nEnergy:5\n"
    assert str(item) == expected_output
    

def test_food_item_creation():
    """Ensure FoodItem initializes correctly."""
    item = FoodItem(food_id=1, x=-2.5, y=3.5, z=4.5, energy=-100)
    assert item.food_id == 1
    assert item.x == -2.5
    assert item.y == 3.5
    assert item.z == 4.5
    assert item.energy == -100  # Energy can be negative


@pytest.mark.parametrize("invalid_id", [-1, "a", None, 3.5])
def test_invalid_food_id(invalid_id):
    with pytest.raises(ValueError):
        FoodItem(food_id=invalid_id, x=1.0, y=2.0, z=3.0, energy=10)
        

@pytest.mark.parametrize("invalid_coord", [["List"],{"Dict":1},("Tuple"),'a', None, "Hello"])
def test_invalid_food_coord(invalid_coord):
    with pytest.raises(ValueError):
        FoodItem(food_id=0, x=invalid_coord, y=2.0, z=3.0, energy=10)