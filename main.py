from graph import Graph
from path import Path
from food_item import FoodItem
from calculation_tester import get_total_cost

def solve(graph : Graph, node : FoodItem) -> None:
    if(len(graph.remaining_food) == 1):
        graph.current_path.path_list.append(node)
        graph.update_optimal()
        return
    
    current_node = node
    graph.remaining_food.remove(current_node)
    graph.current_path.add_to_path(current_node)

    for food in graph.remaining_food:
  
        #curr_food = graph.remaining_food[food.food_id]
        #curr_food = graph.remaining_food[food[0]]
        #next_food = graph.remaining_food[food.food_id + 1]
        #graph.current_path.current_food = curr_food

        curr_path = graph.current_path
        #TESTED UP TO HERE
        cost = get_total_cost(current_node, food)
        if (cost <= curr_path.net_energy_gain):
            net = food.energy - cost
            curr_path.update_net(net)
            solve(graph, food)
            curr_path.update_net(-net)
            graph.remaining_food.add(current_node,current_node.food_id)
        


            


    
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
    starting_node = graph.all_food_nodes[0]
    solve(graph, starting_node)
    print(graph.optimal_path)

if __name__ == "__main__":
    main()



