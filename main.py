from graph import Graph
from path import Path
from food_item import FoodItem
from calculation_tester import get_total_cost

def solve(graph : Graph) -> bool:
    if(len(graph.remaining_food) == 1):
        graph.update_optimal()
        return False
    else:
        for food in graph.remaining_food:
            
            curr_food = graph.remaining_food[food.food_id]
            next_food = graph.remaining_food[food.food_id + 1]
            graph.current_path.current_food = curr_food

            curr_path = graph.current_path
            #TESTED UP TO HERE
            cost = get_total_cost(curr_food, next_food)
            if (cost > curr_path.net_energy_gain):
                return False
            net = next_food.energy - cost
            curr_path.update_net(net)
            curr_path.add_to_path(food)
            solve(graph)


            


    
    """
    if p is solved:
        optimalP = get_optimal(optimalP, p)   
        set p to not solved
    for each move in possible moves for p:
        apply move to p to get p'
        solve(p')
        undo move  # backtrack
    return optimalP
    """
    pass

def main():
    graph = Graph()

    graph.read_csv_data("./random_coordinates_energy.csv")
    graph.initialize_remaining_food()
    graph.current_path.net_energy_gain = graph.remaining_food[0].energy
    solve(graph)

if __name__ == "__main__":
    main()



