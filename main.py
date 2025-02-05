from Path import Path
from FoodItem import FoodItem

def main():
    path = Path()

    path.read_csv_data(filename='./random_coordinates_energy.csv')

    for fooditem in path.food_items:
        print(f"\n{fooditem}\n")
    
    print("Main")


if __name__ == "__main__":
    main()