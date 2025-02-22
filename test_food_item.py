import pytest
from Food_Item import FoodItem

# Test the creation of a FoodItem object with valid inputs.
def test_food_item_creation_integers_positive():
    """Test FoodItem creation."""
    food_item = FoodItem(food_id=1, x=2, y=-3, z=4, energy=5)
    assert food_item.food_id == 1
    assert food_item.x == 2
    assert food_item.y == -3
    assert food_item.z == 4
    assert food_item.energy == 5

# Test the creation of a FoodItem object with valid inputs.
def test_food_item_creation_floats():
    """Test FoodItem creation."""
    food_item = FoodItem(food_id=1, x=-2.1, y=3.2, z=4.3, energy=5)
    assert food_item.food_id == 1
    assert food_item.x == -2.1
    assert food_item.y == 3.2
    assert food_item.z == 4.3
    assert food_item.energy == 5

# Test a variety of invalid inputs to the food_id attribute in the FoodItem class constructor.
# This test uses a pytest decorator to parametrize the test function with a list of invalid inputs.
@pytest.mark.parametrize("invalid_id", [-1, "a", 3.5, [], ()])
def test_invalid_food_id(invalid_id):
    with pytest.raises(ValueError):
        FoodItem(food_id=invalid_id, x=1.0, y=2.0, z=3.0, energy=10)

# Test a variety of invalid inputs to the coordinate attribute in the FoodItem class constructor.
# This test uses a pytest decorator to parametrize the test function with a list of invalid inputs.
@pytest.mark.parametrize("invalid_coord", [[],{},(),'a', "Hello"])
def test_invalid_food_coord(invalid_coord):
    with pytest.raises(TypeError):
        FoodItem(food_id=0, x=invalid_coord, y=2.0, z=3.0, energy=10)

# Test a variety of invalid inputs to the energy attribute in the FoodItem class constructor.
# This test uses a pytest decorator to parametrize the test function with a list of invalid inputs.
@pytest.mark.parametrize("invalid_energy", [[],{},(),'a', "Hello"])
def test_invalid_food_energy(invalid_energy):
    with pytest.raises(TypeError):
        FoodItem(food_id=0, x=1.0, y=2.0, z=3.0, energy=invalid_energy)
